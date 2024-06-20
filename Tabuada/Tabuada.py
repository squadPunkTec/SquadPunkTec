# Tabuada de 1 a 10 usando o laço for em Python

for i in range(1, 11):  # i vai de 1 a 10
    print(f"Tabuada do {i}:")
    for j in range(1, 11):  # j vai de 1 a 10 para multiplicar com i
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # linha em branco para separar cada tabuada
