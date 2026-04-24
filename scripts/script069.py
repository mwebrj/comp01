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
-          69. Criar um programa para imprimir a média aritmética de n números (usar lista)

"""
def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    media = sum(numeros) / len(numeros)
    return media
# Exemplo de uso
numeros = [70, 85, 100, 80, 90]
media = calcular_media(numeros)
print(f"A média aritmética dos números {numeros} é: {media:.2f}")