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
-     34. Criar um programa para imprimir a média aritmética de N números lidos

"""

def media_aritmetica(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

numeros = []
n = int(input("Quantos números deseja inserir? "))
for i in range(n):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
media = media_aritmetica(numeros)
print(f"A média aritmética dos números inseridos é: {media:.2f}")