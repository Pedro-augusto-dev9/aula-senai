#calcular a media de duas notas de um aluno
#entradas
nome = input("informe o nome do aluno: ")
nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))

media = (nota1 + nota2 )/ 2

print(f"a media do aluno {nome} é {media:.2f}")