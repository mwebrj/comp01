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
-     40. Criar um programa para imprimir a soma de todos os múltiplos de 7 que forem pares entre 0 e 1000

"""

def main():
    soma = 0

    for i in range(0, 1001):
        if i % 7 == 0 and i % 2 == 0:
            soma += i

    print(f"A soma de todos os múltiplos de 7 que forem pares entre 0 e 1000 é: {soma}")

main()

