# Função para calcular a similaridade de cossenos
def dot_product(v1, v2):
    """Calcula o produto ponto entre dois vetores."""
    return sum(x * y for x, y in zip(v1, v2))


def vector_norm(v):
    """Calcula a norma de um vetor."""
    return sum(x * x for x in v) ** 0.5


def cos_sim(v1, v2):
    """Calcula a similaridade de cosseno entre dois vetores."""
    return dot_product(v1, v2) / (vector_norm(v1) * vector_norm(v2))


# Definir nomes fictícios e seus gostos musicais
# Dimensões: Rock, Clássica, Pop
pessoa1_nome = "Alice"
pessoa1_rock = 0.8
pessoa1_classica = 0.2
pessoa1_pop = 0.1
embedding1 = [pessoa1_rock, pessoa1_classica, pessoa1_pop]

pessoa2_nome = "Bob"
pessoa2_rock = 0.1
pessoa2_classica = 0.9
pessoa2_pop = 0.2
embedding2 = [pessoa2_rock, pessoa2_classica, pessoa2_pop]

pessoa3_nome = "Carol"
pessoa3_rock = 0.5
pessoa3_classica = 0.3
pessoa3_pop = 0.7
embedding3 = [pessoa3_rock, pessoa3_classica, pessoa3_pop]

# Calcular similaridades
similaridade_1_2 = cos_sim(embedding1, embedding2)
similaridade_1_3 = cos_sim(embedding1, embedding3)
similaridade_2_3 = cos_sim(embedding2, embedding3)

# Imprimir os resultados
print(f"Similaridade entre {pessoa1_nome} e {pessoa2_nome}: {similaridade_1_2:.4f}")
print(f"Similaridade entre {pessoa1_nome} e {pessoa3_nome}: {similaridade_1_3:.4f}")
print(f"Similaridade entre {pessoa2_nome} e {pessoa3_nome}: {similaridade_2_3:.4f}")
