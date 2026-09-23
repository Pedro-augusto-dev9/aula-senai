# Exemplo 3: Lista de compras
produtos = ["Arroz", "Feijão", "Leite", "Café"]
precos = [14.90, 8.50, 5.99, 23.90]
total = 0
print(" --- Lista de compras ---")
for i in range(len(produtos)):
    print(f"{produtos[i]} - R$ {precos[i]:.2f}")
    #exibe cada elemento dos dois vetores (combinação)
    total += precos[i] #acumulando os valores na variável
    # total = total + precos[i]
print(f"\nTotal da compra R$ {total: .2f}")