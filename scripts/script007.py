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
- 7. Criar um programa para ler dois números e imprimir o menor

"""

num1 = int(input("Informe um número: "))
menor = num1
num2 = int(input("Informe o segundo número: "))

if num2 < menor:
    menor  = num2

print(menor)