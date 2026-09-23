# Exemplo 4: Separação de números
numeros = [12, 7, 25, 40, 33, 18, 9, 22]
pares = [] # para os numeros pares
impares = [] #para os numeros impares
# Processamento
for numero in numeros:
    if numero % 2 == 0: # mod: resto da divisão (função para numero par!)
        pares.append(numero) # append => adiciona o valor no vetor
    else:
        impares.append(numero)
print(f"Lista dos números: {numeros}")
print("Números pares:", pares)
print("Números ímpares:", impares)