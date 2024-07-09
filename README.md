# Document Query com Embeddings

Este projeto tem como objetivo fornecer uma ferramenta para consulta de documentos utilizando embeddings para encontrar
os documentos mais relevantes com base em uma consulta de texto. Utiliza-se modelos de embeddings do OpenAI e do
Sentence Transformers para gerar representações vetoriais dos documentos e das consultas, permitindo assim a realização
de buscas semânticas eficientes.

## Funcionalidades

- Geração de embeddings para documentos de texto utilizando modelos do OpenAI e Sentence Transformers.
- Consulta de documentos baseada em similaridade de cossenos entre o embedding da consulta e os embeddings dos
  documentos.
- Cache de embeddings para otimizar consultas subsequentes.

## Requisitos

Para executar este projeto, você precisará ter Python instalado em sua máquina, além das seguintes bibliotecas:

- \`numpy\`
- \`openai\`
- \`sentence-transformers\`

Você pode instalar todas as dependências necessárias utilizando o arquivo \`requirements.txt\`:

```bash
pip install -r requirements.txt
```

Declare a variável de ambiente \`OPENAI_API_KEY\` com a sua chave de API do OpenAI para poder utilizar os modelos de
embeddings da plataforma.

```bash
export OPENAI_API_KEY="sua-chave-de-api"
```

Para obter uma chave de API do OpenAI, acesse o [site da plataforma](https://platform.openai.com/), menu API Keys.

## Uso

Para utilizar a ferramenta, siga os passos abaixo:

1. Clone o repositório para sua máquina local.
2. Instale as dependências utilizando o comando mencionado acima.
3. Execute o script \`main.py\` para iniciar a geração de embeddings e a consulta de documentos.

Exemplo de uso:

```bash
python main.py
```

## Estrutura do Projeto

- \`main.py\`: Script principal que contém a lógica para geração de embeddings e consulta de documentos.
- \`requirements.txt\`: Arquivo com as dependências necessárias para executar o projeto.

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para criar um fork do projeto, fazer suas alterações e enviar um
pull request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo \`LICENSE\` para mais detalhes.