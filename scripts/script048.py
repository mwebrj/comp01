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
-     48. Criar um programa para ler N números e imprimir o maior

"""

def main():
    n = int(input("Quantos números você deseja inserir? "))
    if n <= 0:
        print("Número inválido. Digite um número positivo.")
        return
    maior_num = float('-inf')
    for i in range(n):
        num = float(input(f"Digite o número {i + 1}: "))
        if num > maior_num:
            maior_num = num
    print(f"O maior número inserido é: {maior_num}")
if __name__ == "__main__":
    main()

    