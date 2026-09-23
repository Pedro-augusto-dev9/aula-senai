# Exemplo 5: Lista de tarefas
tarefas = []
# Menu usando o enquanto
while True: # Enquanto for verdadeiro, vai ficar rodando
    print("\n --- Menu ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefa")
    print("3 - Remover tarefa")
    print("0 - Sair")
    opcao = input("Escolha a opção: ")
    if opcao == "1": # "1"
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        print("\n --- Tarefas ---")
        print(tarefa)
    if len(tarefas) == 0:
                print("Nenhuma tarefa cadastrada!")
    elif opcao == "3":
        if len(tarefas) == 0:
                    print("Nenhuma tarefa cadastrada!")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print("\n --- Lista de Tarefas --- ")
                print(f"{i} - {tarefa}")
            try:
                indice = int(input("Digite o número da tarefa para excluir: "))
                if 1 <= indice <= len(tarefas):
                    removida = tarefas.pop(indice -1)
                    print(f"tarefas removidas: {removida}")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Digite um valor válido!")
    elif opcao == "0":
        print("Programa será encerrado!")
        break
    else:
        print("Opção inválida!")