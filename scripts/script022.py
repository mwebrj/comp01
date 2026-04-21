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
-     22. Criar um programa para ler três números e imprimir se o primeiro
é maior ou menor que a soma dos outros dois

"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
somar  = num2 + num3
if num1 > somar:
    print(f"O primeiro número {num1} é maior que a soma dos outros dois {somar}.")

elif num1 == somar:
    print(f"O primeiro número {num1} é igual a soma dos outros dois {somar}.")

else:
    print(f"O primeiro número {num1} é menor que a soma dos outros dois {somar}.")

