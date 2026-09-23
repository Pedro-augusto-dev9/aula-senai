print("programa que classifica um numero")
numero = int(input("informe um nº positivo (>0) e menor que 100: "))
if numero < 0:
    print("vc informou um valor negativo, vou assumir o novo valor")
    numero = 0
elif numero <= 30:
    print("o numeor informado é menor ou igual a 30")
elif numero >30 and numero <=70:
    print("o numeor informado é menor ou igual a 30")
elif numero == 90:
    print("o numero é 90")
elif numero > 100:
    print("numero será 100")
    numeor = 100
else:
    print("o nº é maior que 70 e menor que 100")