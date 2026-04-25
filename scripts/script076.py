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
-          76. Ler um número que representa a ordem de uma matriz quadrada e crie um quadrado mágico, 
onde a soma das linhas, colunas e diagonais é constante e com o mesmo valor

"""

def criar_quadrado_magico(n):
    if n % 2 == 0:
        raise ValueError("A ordem do quadrado mágico deve ser ímpar.")
    
    quadrado = [[0] * n for _ in range(n)]
    
    num = 1
    i, j = 0, n // 2
    
    while num <= n * n:
        quadrado[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        if quadrado[new_i][new_j] != 0:
            i += 1
        else:
            i, j = new_i, new_j
    
    return quadrado
def imprimir_quadrado(quadrado):
    for linha in quadrado:
        print(linha)
n = int(input("Digite a ordem do quadrado mágico (número ímpar): "))
quadrado_magico = criar_quadrado_magico(n)
imprimir_quadrado(quadrado_magico)
