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