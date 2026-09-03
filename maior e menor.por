programa {
	funcao inicio() {
		inteiro num[2][2]
		inteiro i, j
		inteiro maior, menorValor
		inteiro linhamaior = 0, colunamaior = 0
		inteiro linhamenor = 0, colunamenor = 0

		// 1. Passo: Leitura dos dados da matriz
		para(i = 0; i < 2; i++){
			para(j = 0; j < 2; j++){
				escreva("Escreva um valor para [", i, "][", j, "]: ")
				leia(num[i][j])
			}
		}

		// 2. Passo: Inicializa o maior e o menor com o primeiro elemento da matriz
		maior = num[0][0]
		menorValor = num[0][0]

		// 3. Passo: Varredura para encontrar os extremos e suas posições
		para(i = 0; i < 2; i++){
			para(j = 0; j < 2; j++){
				
				// Verifica se encontrou um novo maior valor
				se(num[i][j] > maior){
					maior = num[i][j]
					linhamaior = i
					colunamaior = j
				}
				
				// Verifica se encontrou um novo menor valor (Sinal corrigido: < )
				se(num[i][j] < menorValor){
					menorValor = num[i][j]
					linhamenor = i
					colunamenor = j
				}
			}
		}

		// 4. Passo: Exibição dos resultados (Fora do laço 'para')
		escreva("\n-----------------------------")
		escreva("\nMenor valor: ", menorValor, " na posicao [", linhamenor, "][", colunamenor, "]")
		escreva("\nMaior valor: ", maior, " na posicao [", linhamaior, "][", colunamaior, "]")
		escreva("\n-----------------------------")
	}
}
