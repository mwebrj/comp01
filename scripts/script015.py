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
-     15. Criar um programa para ler dois números e dizer quanto o segundo representa em percentual do primeiro.

"""
num1 = float(input("Informe o número: "))
num2 = float(input("Informe o segundo número: "))

print(f"{num1}/{num2} = {num1/num2*100:.2f}%")