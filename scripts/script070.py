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
-          70. Criar um programa para imprimir o produto de todos os números de uma lista

"""
def produto_lista(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto
# Exemplo de uso
numeros = [3, 4, 2, 3]
resultado = produto_lista(numeros)
print("O produto dos números da lista é:", resultado)
