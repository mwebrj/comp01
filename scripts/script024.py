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
-     24. Criar um programa para ler três números que representam os coeficientes
de uma equação do segundo grau, imprima as raízes dessa equação

"""
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
delta = b**2 - 4*a*c
if delta > 0:
    raiz1 = (-b + delta**0.5) / (2*a)
    raiz2 = (-b - delta**0.5) / (2*a)
    print(f"As raízes da equação do segundo grau são: {raiz1} e {raiz2}.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"A equação do segundo grau tem uma raiz real: {raiz}.")
else:
    print("A equação do segundo grau não tem raízes reais.")
    