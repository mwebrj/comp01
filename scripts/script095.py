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
-	95. Crie uma função que receba números inteiros até que o usuário digite “fim” e imprima o antecessor e o sucessor do número recebido e indique se o número lido é par ou ímpar
"""
def is_even(num):
    return num % 2 == 0
while True:
    user_input = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if user_input.lower() == "fim":
        break
    try:
        number = int(user_input)
        predecessor = number - 1
        successor = number + 1
        parity = "par" if is_even(number) else "ímpar"
        print(f"Número: {number}, Antecessor: {predecessor}, Sucessor: {successor}, Paridade: {parity}")
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")
        