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
-     30. Criar um programa para ler um número float e imprimir a parte inteira e a parte fracionária

"""

num = float(input("Digite um número float: "))
parte_inteira = int(num)
parte_fracionaria = num - parte_inteira
print(f"A parte inteira do número é: {parte_inteira}")
print(f"A parte fracionária do número é: {parte_fracionaria:.2f}")