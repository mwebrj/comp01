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
-     47. Criar um programa para ler um número e imprimir o maior número cujo quadrado é menor que o número lido

"""
import math
def main():
    num = float(input("Digite um número: "))
    if num < 0:
        print("Número inválido. Digite um número não negativo.")
        return
    maior_num = math.floor(math.sqrt(num))
    print(f"O maior número cujo quadrado é menor que {num} é: {maior_num}")
if __name__ == "__main__":
    main()