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
78. Se a ordem lida for 4 a matriz final deverá ser:
       0  1  2  3
       11 12 13 4
       10 15 14 5
       9  8  7  6

"""
def criar_matriz_espiral(n):
    matriz = [[0] * n for _ in range(n)]
    num = 0
    for i in range((n + 1) // 2):
        for j in range(i, n - i):
            matriz[i][j] = num
            num += 1
        for j in range(i + 1, n - i):
            matriz[j][n - i - 1] = num
            num += 1
        for j in range(n - i - 2, i - 1, -1):
            matriz[n - i - 1][j] = num
            num += 1
        for j in range(n - i - 2, i, -1):
            matriz[j][i] = num
            num += 1
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(' '.join(map(str, linha)))
def main():
    n = int(input("Digite a ordem da matriz quadrada: "))
    matriz_espiral = criar_matriz_espiral(n)
    imprimir_matriz(matriz_espiral)
if __name__ == "__main__":
    main()