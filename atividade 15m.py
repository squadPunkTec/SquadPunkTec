from faker import Faker
import random

# Inicializa o Faker
fake = Faker()

# Gera nome aleatório
nome = fake.name()

# Gera cidade aleatória
cidade = fake.city()

# Gera idade aleatória entre 18 e 80 anos
idade = random.randint(18, 80)

# Exibe os dados gerados
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")

