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
-     26. Criar um programa para ler dois números e imprimir o MDC e o MMC

"""
# Calculo do MDC de dois números: 
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mmc(a, b):
    return (a * b) // mdc(a, b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"O MDC de {num1} e {num2} é: {mdc(num1, num2)}")
print(f"O MMC de {num1} e {num2} é: {mmc(num1, num2)}")

