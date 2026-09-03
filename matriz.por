programa {
  funcao inicio() {

    inteiro mat[2][2]
    inteiro i, j
    cadeia resposta
    inteiro valor_somado
    

  escreva("quer entrar no sistema [s][?]: ")
  leia(resposta)

  escreva("===================================\n")
  escreva("        BEM-VINDO AO PROGRAMA      \n")
  escreva("===================================\n")
  
  escreva("informe o valor para somar: ")
  leia(valor_somado)
  se(resposta == ("s") ou resposta == ("S")){
  
  para(i = 0; i< 2; i++){
    para(j = 0; j< 2; j++){
      escreva("\nescreva o ", j + 1, "º elemneto de ", i + 1, ": ")
      leia(mat[i][j])

      mat[i][j] = mat[i][j] + valor_somado
    }
  }
  para(i=0;i<2;i++){
    para(j = 0; j< 2; j++){
      escreva("\nMatriz: ", i + 1, "ª linha: ", mat[i][j], " ")
      

    }
    escreva("\n")
  }
  
  }senao{
    escreva("programa encerrado")
    
    }//fim de SENAO
  
  }
}
