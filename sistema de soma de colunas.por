programa {
  funcao inicio() {

    inteiro mat[2][2]
    inteiro i, j
    cadeia resposta
    inteiro valor_somado
    inteiro soma[2] // ter o mesmo tamanho das linhas da matriz
    
    

  escreva("quer entrar no sistema [s][?]: ")
  leia(resposta)
  se(resposta == ("s") ou resposta == ("S")){


  escreva("===================================\n")
  escreva("        BEM-VINDO AO PROGRAMA      \n")
  escreva("===================================\n")
  
  
  para(i = 0; i< 2; i++){
    soma[i] = 0
    para(j = 0; j< 2; j++){
      escreva("\nescreva o ", j + 1, "º elemneto de ", i + 1, ": ")
      leia(mat[i][j])

      soma[i] = soma[i] + mat[i][j]
    }
  }
  
  escreva("exibindo a matriz")
  para(i=0;i<2;i++){
    para(j = 0; j< 2; j++){
      escreva("\nMatriz: ", i + 1, "ª linha: ", mat[i][j], " ")
      

    }
    escreva("\n")}
  
  escreva("\n------- a soma das linhas da matriz foi-----\n")
    para(i=0;i<2;i++){
      escreva("[", soma[i], "]")}// final do para
    }
  }
}
