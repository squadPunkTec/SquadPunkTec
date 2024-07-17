import pandas as pd

# Criando o DataFrame inicial
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'José', 'Carla', 'Mariana'],
    'Idade': [45, 30, 22, 50, 35, 27, 55],
    'Renda': [4000, 6000, 3000, 20000, 8000, 12000, 1500],
}

df = pd.DataFrame(dados)

# Filtrando as pessoas com idade maior que 40 anos
filtro_idade_40 = df[df['Idade'] > 40]

# Filtrando as pessoas com renda maior que 5 mil
filtro_renda_5k = df[df['Renda'] > 5000]

# Filtrando as pessoas com renda maior que 15 mil
filtro_renda_15k = df[df['Renda'] > 15000]

# Exibindo os resultados
print("Pessoas com idade maior que 40 anos:")
print(filtro_idade_40)
print("\nPessoas com renda maior que 5 mil:")
print(filtro_renda_5k)
print("\nPessoas com renda maior que 15 mil:")
print(filtro_renda_15k)
