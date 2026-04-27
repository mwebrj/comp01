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
-	94. Crie uma função que receba números inteiros até que o usuário digite “fim” e imprima ao final todos os números digitados que são primos
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
while True:
    user_input = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if user_input.lower() == "fim":
        break
    try:
        number = int(user_input)
        if is_prime(number):
            print(f"{number} é um número primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")
        