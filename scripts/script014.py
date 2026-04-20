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
-     14. Criar um programa para ler dois números que representam os valores dos catetos 
de um triângulo retângulo e imprimir o valor da hipotenusa (a2 = b2 + c2)

"""
cateto1 = float(input(" Informe o cateto 01: "))
cateto2 = float(input(" Informe o cateto 02: "))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f"Hipotenusa: {hipotenusa:.2f}")