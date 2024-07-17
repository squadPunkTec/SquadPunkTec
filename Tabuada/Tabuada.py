# Tabuada de 1 a 10 usando o laço for em Python

for i in range(1, 11):  # i vai de 1 a 10
    print(f"Tabuada do {i}:")
    for j in range(1, 11):  # j vai de 1 a 10 para multiplicar com i
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # linha em branco para separar cada tabuada

    import pandas as pd

# Dados fornecidos (reduzido para manter o exemplo mais compacto)
dados = {
    'nome': ["Rafaela Rezende", "Srta. Beatriz das Neves", "Ana Clara das Neves", "Olivia Silva", "Alexia Martins", 
             "Lorena Almeida", "Julia Freitas", "Thiago Novaes", "Maria Sophia Pires", "Emilly Carvalho", 
             "Rodrigo Melo", "Sr. Caio Gonçalves", "Sr. Francisco Ramos", "Joaquim Duarte", "Pedro Henrique Barbosa"],
    'idade': [46, 24, 28, 23, 54, 66, 63, 46, 28, 63, 29, 22, 19, 65, 49, 61],
    'renda': [15594.52, 16478.26, 13729.48, 18478.46, 9988.47, 2224.67, 2451.84, 16897.84, 7059.64, 11843.88, 
              2777.63, 2869.68, 14668.3, 14678.66, 3319.36, 7437.54]
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Aplicando filtro com idade > 40 e renda > 5000 ou renda > 15000
dados_filtrados = df[(df['idade'] > 40) & ((df['renda'] > 5000) | (df['renda'] > 15000))]

# Exibindo os dados filtrados
print("Pessoas filtradas:")
print(dados_filtrados)

