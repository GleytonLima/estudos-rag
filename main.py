import hashlib
import json
import os
from typing import List

import numpy as np
from openai import OpenAI
from sentence_transformers import util, SentenceTransformer


# vamos criar um enum para os modelos de embedding
class EmbeddingModel:
    OPENAI = "openai"
    SENTENCE_TRANSFORMER = "sentence-transformer"


class OpenAIEmbeddingGenerator:
    def __init__(self, model="text-embedding-3-large"):
        self.openai_client = OpenAI()
        self.model = model

    def generate_embeddings(self, documents: List[str]) -> List[dict]:
        response = self.openai_client.embeddings.create(input=documents, model=self.model)
        return [{"id": doc, "embedding": r.embedding} for doc, r in zip(documents, response.data)]


class SentenceTransformerEmbeddingGenerator:
    def __init__(self, model="paraphrase-MiniLM-L6-v2"):
        self.model = model

    def generate_embeddings(self, documents: List[str]) -> List[dict]:
        model = SentenceTransformer(self.model)
        return [{"id": doc, "embedding": model.encode(doc).tolist()} for doc in documents]


class EmbeddingGenerator:
    def __init__(self, model=EmbeddingModel.OPENAI):
        self.openai_client = OpenAI()
        self.model = model

    def generate_embeddings(self, documents: List[str]) -> List[dict]:
        documents = [doc.replace("\n", " ") for doc in documents]
        key = hashlib.sha256("".join(documents).encode('utf-8')).hexdigest()
        cache_file = f"embeddings_{self.model}_{key}.json"

        if os.path.exists(cache_file):
            return self._load_embeddings_from_file(cache_file)

        embeddings = self._fetch_embeddings(documents)
        self._save_embeddings_to_file(cache_file, embeddings)
        return embeddings

    def _fetch_embeddings(self, documents: List[str]) -> List[dict]:
        if self.model == EmbeddingModel.OPENAI:
            return OpenAIEmbeddingGenerator().generate_embeddings(documents)
        elif self.model == EmbeddingModel.SENTENCE_TRANSFORMER:
            return SentenceTransformerEmbeddingGenerator().generate_embeddings(documents)
        else:
            raise ValueError(f"Model {self.model} not supported")

    @staticmethod
    def _load_embeddings_from_file(filename: str) -> List[dict]:
        with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def _save_embeddings_to_file(filename: str, embeddings: List[dict]):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(embeddings, file, ensure_ascii=False)


class DocumentQuery:
    def __init__(self, embeddings: List[dict], documents: List[str]):
        self.embeddings = embeddings
        self.documents = documents

    def query(self, query_text: str, top_k: int = 3):
        query_embedding = np.asarray(EmbeddingGenerator().generate_embeddings([query_text]))
        scores = util.cos_sim([q['embedding'] for q in query_embedding], [e['embedding'] for e in self.embeddings])[0]
        top_indices = np.argsort(-scores)[:top_k]

        print(f"Query: {query_text}")
        for idx in top_indices:
            print(f"Score: {scores[idx]:.4f}")
            print(self.documents[idx])
            print("--------")


if __name__ == '__main__':
    texts = [
        "O gato (nome científico: Felis silvestris catus) ou gato doméstico é um mamífero carnívoro da família dos felídeos, muito popular como animal de estimação...",
        "O cão (nome científico: Canis lupus familiaris), no Brasil também chamado de cachorro, é um mamífero carnívoro da família dos canídeos..."
    ]

    embedding_generator = EmbeddingGenerator()
    embeddings = embedding_generator.generate_embeddings(texts)
    document_query = DocumentQuery(embeddings, texts)
    document_query.query("É um animal que faz au au")
