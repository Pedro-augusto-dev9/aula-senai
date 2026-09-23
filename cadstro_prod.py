produtos = {
  "Alface": 4.50,
  "Tomate (kg)": 8.90,
  "Batata (kg)": 7.50,
  "Carne Moída (kg)": 42.00,
  "Peito de Frango (kg)": 21.00,
  "Leite (Litro)": 5.80,
  "Queijo Muçarela (200g)": 11.00,
  "Arroz (5kg)": 29.90,
  "Feijão (1kg)": 9.50,
  "Macarrão": 4.50,
  "Café (500g)": 19.50,
  "Detergente": 2.50,
  "Sabão em Pó": 14.90,
  "Papel Higiênico (12 un)": 16.50,
  "Creme Dental": 4.50,
  "Sabonete": 3.00
}

print("--- cadastro de produtos ---")
for produto, preco in produtos.items():
    print(f"produto: {produto} - R${preco:.2f}")

print("\n consultar um produto")
nome = input("digite o nome do produto: ")

if nome in produtos:
    #print(f"preco: R$ {preco:.2f}")
    print(f"preco: R$ {produtos[nome]:.2f}")
else:
    print("produto não localizado")
