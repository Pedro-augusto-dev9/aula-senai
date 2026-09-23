estoque = {
    "teclado" : {
        "preco" : 120.00,
        "quantidade" : 10
    },
    "mouse": {
        "preço": 65.50,
        "quantidade": 15
    },
    "Monitor": {
        "preco": 850.00,
        "quantidade": 5
    }
}
while True:
    print("\n --- Estoque ---")
    print("1 - Listar produtos")
    print("2 - Consultar produtos")
    print("3 - Adicionar estoque")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        for produto, dados in estoque.items():
            print(
                f"{produto} |"
                f"R$ {dados['preco']:.2f}"
                f"Quantidade: {dados['quantidade']}"
            )
    elif opcao == "2":
        nome = input("Digite o produto: ")
        if nome in estoque:
            dados = estoque[nome]
            print(f"Preço: R$ {dados['preco']:.2f}")
            print(f"Quantidade: {dados['quantidade']:.2f}")
    elif opcao == "3":
        nome = input("Digite o produto: ")
        if nome in estoque:
            dados = estoque[nome]
            print(f"Preço: R$ {dados['preco']:.2f}")
            print(f"Quantidade: {dados['quantidade']:.2f}")