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
-     28. Criar um programa para ler três números que representam os lados de um triângulo, imprimir se é equilátero, isósceles ou escaleno.

"""
# Ler os lados do triângulo do usuário
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if ((lado1 + lado2) < lado3) or ((lado1 + lado3) < lado2) or ((lado2 + lado3) < lado1):
    print("Não pode ser triângulo...")
# Verificar o tipo do triângulo
elif lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")