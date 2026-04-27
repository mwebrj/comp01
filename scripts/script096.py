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
-	96. Crie um programa que leia números inteiros até que o usuário digite “fim” e calcule
a média dos números lidos
"""

total = 0
count = 0
while True:
    user_input = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if user_input.lower() == "fim":
        break
    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

if count > 0:
    average = total / count
    print(f"A média dos números lidos é: {average}")
else:
    print("Nenhum número válido foi digitado.")
    