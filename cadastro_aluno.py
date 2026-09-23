# Exemplo 1: Cadastro de alunos
alunos = [] # vetor
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ") # i = 0, 0+1 = 1º aluno
    alunos.append(nome)
print("\n --- Alunos Cadastrados ---")
i=0
for aluno in alunos:
    i = i+1
    print(i , " ", aluno)
    