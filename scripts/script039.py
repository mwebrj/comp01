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
-     39. Criar um programa para imprimir a média aritmética dos números primos de 0 a 100

"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    primes = []
    for i in range(101):
        if is_prime(i):
            primes.append(i)

    if primes:
        media = sum(primes) / len(primes)
        print(f"A média aritmética dos números primos de 0 a 100 é: {media}")
    else:
        print("Não há números primos no intervalo.")

main()