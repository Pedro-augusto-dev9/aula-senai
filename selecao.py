
def inicio():
    print("programa que verifica a idade da pessoa")
    idade = int(input(" informe a sua idade: "))
    if idade >= 18:
        print("idade maior ou igual a 18 anos")
        estado = input("informe o estado: ")
    else:
        print("voce possui menos de 18 anos")
        cor = input("informe o nome da cor: ")
    
    return idade

def processamento(idade):
    cnh = input("voce ja possui carteira de habilitação?[s],[n]: ")
    if cnh == "S" or cnh == "s":
        print("SIM")
        possui = "possui"
    else:
        print("NÃO")
        possui = "não possui"

    print(f"bem-vindo! Voce possui {idade} anos e voce {possui} CNH")

    #opcao = input("deseja continuar?: ")
    #if opcao == "S" or "s":
funcao = inicio()
processamento(funcao)
