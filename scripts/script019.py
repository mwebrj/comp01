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
-     19. Criar um programa para ler dois números que representam os lados de um
retângulo, imprima o perímetro e a área

"""
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
perimetro = 2 * (base + altura)
area = base * altura
print("O perímetro do retângulo é:", perimetro)
print("A área do retângulo é:", area)
