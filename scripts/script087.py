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
-	87. Ler um número inteiro e imprimir a soma dos dígitos do número.
"""
def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total
# Solicitar ao usuário que digite um número inteiro
user_input = int(input("Digite um número inteiro: "))
# Imprimir a soma dos dígitos do número
print("A soma dos dígitos do número é:", sum_of_digits(user_input))
