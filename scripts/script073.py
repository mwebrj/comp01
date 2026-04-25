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
-          73. Criar um programa para imprimir os números da diagonal principal de 
uma matriz NxN

"""
import random

def valor():
    num = random.randint(1, 100)
    return num

def diagonal_principal(matriz):
    if not matriz or len(matriz) != len(matriz[0]):
        return None  # Retorna None se a matriz não for quadrada
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
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
resultado = diagonal_principal(matriz)
print("Os números da diagonal principal são:", resultado)
