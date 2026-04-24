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
-      54. Criar um programa que receba dois pares de números que representam 
dois pontos em uma reta e imprima os valores dos coeficientes da equação da reta (y = ax + b)

"""
# Recebe os pontos
x1, y1 = map(float, input("Digite o primeiro ponto (x1 y1): ").split())
x2, y2 = map(float, input("Digite o segundo ponto (x2 y2): ").split())

# Calcula os coeficientes da reta
a = (y2 - y1) / (x2 - x1)  # Coeficiente angular
b = y1 - a * x1  # Coeficiente linear

print(f"Coeficiente angular (a): {a}")
print(f"Coeficiente linear (b): {b}")
