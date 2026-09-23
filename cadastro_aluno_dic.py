# Criação do dicionário com as vírgulas e a nota como número (float)
aluno = { 
    "nome": "Carlos", 
    "idade": "17", 
    "curso": "ADS", 
    "nota": 8.5 
}

# Exibição dos dados
print("--- dados do aluno ---")
print(f"nome: {aluno['nome']}")
print(f"idade: {aluno['idade']}")
print(f"curso: {aluno['curso']}")
print(f"nota: {aluno['nota']:.2f}")
