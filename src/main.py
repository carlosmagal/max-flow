import numpy as np
from simplex import Simplex, printOtimo, pivotingAuxiliar, getInput
# N 0 = 0
# I I   X

def main():

  n, m,  matrixAuxiliar, arrayC = getInput()

  n = n - 2 + m
  m += m

  simplex1 = Simplex(n, m+n, matrixAuxiliar, matrixAuxiliar)

  result = simplex1.runAuxiliar()
  if result == 0:#otimo

    for i in range(m+n, n+n+m):# deletando coluna de variaveis auxiliares
      matrixAuxiliar = np.delete(matrixAuxiliar, n+m, 1)

    for i in range(n):#deletando vero da auxiliar
      matrixAuxiliar = np.delete(matrixAuxiliar, 0, 1)

    matrixAuxiliar = np.append(np.vstack([np.zeros(n), np.identity(n)]), matrixAuxiliar, axis=1)#colocando novo vero na matriz

    # arrayC = arrayC * -1#multiplicando c por -1

    matrixAuxiliar[0] = arrayC #colocando c linha 0 da matriz

    maxZeros = n-1
    maxOnes = 1
    
    for i in range(n, n+m+1):#pivotendo a linha 0 de acordo com as bases
      for j in range(1,n+1):
        if matrixAuxiliar[j][i] == 0:
          maxZeros = maxZeros-1
        elif matrixAuxiliar[j][i] == 1:
          maxOnes = maxOnes-1
        else:
          break
      else:
        if maxOnes == 0 and maxZeros == 0:
          matrixAuxiliar = pivotingAuxiliar(matrixAuxiliar, n, m, i)
        maxZeros = n-1
        maxOnes = 1

    simplex2 = Simplex(n, m, matrixAuxiliar, matrixAuxiliar)
    
    if simplex2.run():#rodando simplex fase 2
      
      print('otima')
      print(np.around(matrixAuxiliar[0][n+m],7))
      # print(otimo.transpose())
      printOtimo(matrixAuxiliar, n, m)
      print(*np.around(matrixAuxiliar[0][0:n],7))

    else: 
      print('ilimitada')
      printOtimo(matrixAuxiliar, n, m)
      print(*np.around(matrixAuxiliar[0][0:n],7))


  elif result == 1:#inviavel
    print('inviavel')
    print(*np.around(matrixAuxiliar[0][0:n],7))

  else:#ilimitada
    print('ilimitada')
    printOtimo(matrixAuxiliar, n, m)
    print(*np.around(matrixAuxiliar[0][0:n],7))


main()