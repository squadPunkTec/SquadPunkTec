import pandas as pd

# Criando o DataFrame
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'José', 'Carla', 'Mariana'],
    'Idade': [25, 30, 22, 28, 35, 27, 31],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(dados)

# Filtrando os moradores do Recife
moradores_recife = df[df['Cidade'] == 'Recife']

# Exibindo o DataFrame filtrado
print("Moradores do Recife:")
print(moradores_recife)
