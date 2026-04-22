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
-     35. Criar um programa para imprimir o produto de N números lidos

"""

def main():
    n = int(input("Digite a quantidade de números: "))
    produto = 1

    for i in range(n):
        numero = float(input(f"Digite o número {i + 1}: "))
        produto *= numero

    print(f"O produto dos {n} números é: {produto}")

main()