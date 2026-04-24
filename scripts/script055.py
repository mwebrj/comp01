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
-      55. Criar um programa para ler dois números que representam os catetos de um
triângulo retângulo. Calcule a hipotenusa e imprima o valor do seno, cosseno, 
tangente, cotangente, secante e cossecante dos dois ângulos formados pelos catetos.

"""

import math
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
seno1 = cateto1 / hipotenusa
cossecante = hipotenusa / cateto1
cosseno1 = cateto2 / hipotenusa
secante = hipotenusa / cateto2
tangente1 = cateto1 / cateto2
cotangente = cateto2 / cateto1

print(f"Base = {cateto1:.2f}\tAltura = {cateto2:.2f}")
print(f"Hipotenusa = {hipotenusa:.2f}")

print(f"Seno do primeiro ângulo: {seno1:.2f}")
print(f"Cosseno do primeiro ângulo: {cosseno1:.2f}")
print(f"Tangente do primeiro ângulo: {tangente1:.2f}")

print(f"Cotangente do primeiro ângulo: {cotangente:.2f}")
print(f"Secante do primeiro ângulo: {secante:.2f}")
print(f"Cossecante do primeiro ângulo: {cossecante:.2f}")
