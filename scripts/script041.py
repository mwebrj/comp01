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
-     41. Criar um programa para imprimir o fatorial do número

"""
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

num = int(input("Digite um número para calcular o fatorial: "))
if num < 0:
    print("O fatorial não é definido para números negativos.")
else:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é: {resultado}")


