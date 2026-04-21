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
-     20. Criar um programa para ler o raio de um círculo e imprimir o perímetro
e a área

"""
PI = 3.14159
raio = float(input("Digite o raio do círculo: "))
perimetro = 2 * PI * raio
area = PI * raio ** 2
print("O perímetro do círculo é:", perimetro)
print("A área do círculo é:", area)
