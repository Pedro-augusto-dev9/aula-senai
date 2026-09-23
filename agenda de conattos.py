#agenda de contatos
contatos = {
    "Carlos" : {
        "telefone" : "51 999999999",
        "email" : "carlos@local.com"
    },
    "Mariana" : {
        "telefone" : "51 888888888",
        "email" : "mariana@local.com"
    }
}
print("\n --- agenda de contatos ---")
#buscar os dados do dicionario
#primeiro campo chamado de nome
#segundo campo chamado de dados por armazenar informações da pessoa
#terceiro campo chamado de 
    #1º     #2º        #3º
for nome, dados in contatos.items():
    print(f"\nNome: {nome}")
    print(f"\nTelefone: {dados['telefone']}")
    print(f"\nEmail: {dados['email']}")
    print("-----------------------------------")
#Processamento
#buscar por uma pessoa no dicionario
nome = input("digite o nome da pessoa: ")
# busca no dicionario
if nome in contatos:
    contato = contatos[nome]
    print(f"telefone: {contato['telefone']}")
    print(f"E-mail: {contato['email']}")
else:
    print("nome não localizado")