"""
UFRJ - Universidade Federal do Rio de Janeiro

Curso : Engenharia Matemática
Disciplina : Computação 01
Professor : Henrique Tavares
Atividade : Avaliação P01

- Resolver estes 100 scripts em Python utilizando o github

Graduando : Marcio AS Coelho
DRE : 126049099
Github : @mwebrj

Script :
-          74. Criar um programa para imprimir os números da diagonal secundária de uma matriz NxN

"""
import random
def valor():
    num = random.randint(1, 100)
    return num

def diagonal_secundaria(matriz):
    if not matriz or len(matriz) != len(matriz[0]):
        return None  # Retorna None se a matriz não for quadrada
    diagonal = []
    n = len(matriz)
    for i in range(n):
        diagonal.append(matriz[i][n - 1 - i])
    return diagonal

# Exemplo de uso
valorN = int(input("Informe o valor de N: "))
matriz = []
if valorN <= 1:
    print("O valor de N deve ser maior que 1.")
else:
    for i in range(valorN):
        linha = []
        for j in range(valorN):
            linha.append(valor())
        matriz.append(linha)
    
print(matriz)
resultado = diagonal_secundaria(matriz)
print("Os números da diagonal secundária são:", resultado)
