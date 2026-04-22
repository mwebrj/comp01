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
-     46. Criar um programa para imprimir o número primo mais próximo de um número informado

"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def closest_prime(n):
    if n < 2:
        return 2
    lower = n - 1
    upper = n + 1
    while True:
        if is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        lower -= 1
        upper += 1
number = int(input("Digite um número: "))
print(closest_prime(number))
