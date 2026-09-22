#comentario
#programa para calcular o valor da compra
#entradas (input): preço e quantida
print("programa que calcula o valor da coimpra")
preco = float(input("informe o valor do produto: "))
quantidade = int(input("informe a quantidade: "))
#processamentos: preço * quantidade
total = preco * quantidade
#saídas: valor total - formatada com duas casas decimais
print(f"o valor total {total:.2f}")