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
-          59. Crie uma função (def) que receba um número float indicando uma temperatura em Celsius e imprima seu valor em Kelvin

"""
def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    print(f"{celsius}°C é igual a {kelvin}K")

frase = "-"
print(f"\n{frase*50}\nFunção para converter Celsius para Kelvin\n{frase*50}")
celsius_para_kelvin(26)