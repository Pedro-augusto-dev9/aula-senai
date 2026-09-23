# Exemplo 8: Boletim escolar
aluno = {
    "nome": "Mariana",
    "notas" : [8.0, 7.5, 9.0, 6.5]
}
# copiamos as notas do dicionario (campo notas) para o vetor notas
notas = aluno["notas"] # acumula as notas
media = sum(notas)/len(notas) #medias das notas
print("\n --- Boletim escolar ---")
# notas é o vetor
# nota é o campo/elemento do vetor de notas
for i, nota in enumerate(notas, start=1):
    print (f"Nota: {i}: {nota:.2f}")
# exibe a média do aluno
print (f"\nMédia: {media:.2f}")

if media >=7:
    print("Aprovado!")