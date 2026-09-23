print("oprogram que testa os tres numeros inteiros e mostra o maior valor")

# entrada

n1 = int(input("Informe o 1º valor: "))
n2 = int(input("Informe o 2º valor: "))
n3 = int(input("Informe o 3º valor: "))

# processamento
if n1 < 0 or n2 < 0 or n3 < 0:
    print("voce informou um valor inválido")
    exit()
if n1 > n2 and n1 > n3:
    print("o 1º numero é maior")
if n2 > n1 and n2 > n3:
    print("o 2º numero é maior")
if n3 > n1 and n3 > n2:
    print("o 3º numero é maior")
if n1 == n2 and n2 == n3 and n1 == n3:
    print("os nº são iguais")
    exit()