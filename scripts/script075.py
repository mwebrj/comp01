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
-          75. Calcular a multiplicação de duas matrizes NxN

"""
import random
def valor():
    num = random.randint(1, 30)
    return num

def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(valor())
        matriz.append(linha)
    return matriz

def multiplicacao_matrizes(matriz_a, matriz_b):
    n = len(matriz_a)
    resultado = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    return resultado

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
n = int(input("Digite a ordem da matriz quadrada: "))
matriz_a = criar_matriz(n)
matriz_b = criar_matriz(n)
print(f"A:\n{matriz_a}")
print(f"B:\n{matriz_b}")
resultado = multiplicacao_matrizes(matriz_a, matriz_b)
imprimir_matriz(resultado)

