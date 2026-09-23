<<<<<<< HEAD
# Exemplo 2: Média de notas
notas = [7.5, 8.0, 6.5, 9.0, 5.5]
soma = sum(notas) # faz a soma dos valores do vetor
media = soma / len(notas) # usando o len (quantidade)
print("\n --- Notas ---")
# for i in range (5) -> entrar dados
for nota in notas: #buscar as notas no vetor
    print(f"Nota: {nota:.2f}")

print(f"\nSoma das notas: {soma:.2f}")
print(f"\nA média da turma: {media:.2f}")
=======
#calcular a media de duas notas de um aluno
#entradas
nome = input("informe o nome do aluno: ")
nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))

media = (nota1 + nota2 )/ 2

print(f"a media do aluno {nome} é {media:.2f}")
>>>>>>> ca01621c22d00b3bedaec5429e03fe70519af07b
