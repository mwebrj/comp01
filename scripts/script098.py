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
-	98. Crie um programa que leia números inteiros até que o usuário digite “fim” e 
calcule a soma dos pares, a média dos ímpares e liste todos os números primos lidos
"""

from scripts.script039 import is_prime


def main():
    even_sum = 0
    odd_sum = 0
    odd_count = 0
    primes = []

    while True:
        user_input = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if user_input.lower() == "fim":
            break
        
        try:
            number = int(user_input)
            if number % 2 == 0:
                even_sum += number
            else:
                odd_sum += number
                odd_count += 1
            
            if is_prime(number):
                primes.append(number)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    odd_average = odd_sum / odd_count if odd_count > 0 else 0

    print(f"Soma dos números pares: {even_sum}")
    print(f"Média dos números ímpares: {odd_average}")
    print(f"Números primos lidos: {primes}")
    