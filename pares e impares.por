programa {
  funcao inicio() {
    inteiro num[2][2]
    inteiro i, j
    inteiro somar = 0, somar_impar = 0
    inteiro contar_pares = 0, contar_impares = 0

    para(i = 0; i< 2; i++){
      para(j = 0; j< 2; j++){
        escreva("\nescreva o ", j + 1, "º elemneto de ", i + 1, ": ")
        leia(num[i][j])
        se(num[i][j] % 2 == 0){
          contar_pares ++
          somar = somar + num[i][j]
        }senao{
          contar_impares ++
          somar_impar = somar_impar + num[i][j]
        }
        }
    }
      para(i = 0; i< 2; i++){
        para(j = 0; j< 2; j++){
          escreva(num[i][j], "\t")
      }
      escreva("\n")
      }
        escreva("quantidades de pares: ",contar_pares, "\n")
        escreva("soma de pares: ",somar, "\n")
        escreva("quantidades de impares: ",contar_impares, "\n")
        escreva("soma de impares: ",somar_impar, "\n")
      
  }
}
