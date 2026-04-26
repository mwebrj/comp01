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
-	79. Criar um programa para imprimir a decomposição em fatores primos de um número dado

"""
def fatoracao_primos(n):
    fatores = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return fatores
numero = int(input("Digite um número para decompor em fatores primos: "))
fatores_primos = fatoracao_primos(numero)
print(f"A decomposição em fatores primos de {numero} é: {fatores_primos}")
