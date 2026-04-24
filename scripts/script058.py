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
-          58. Crie uma função (def) que receba um número float indicando uma temperatura em Celsius e imprima seu valor em Fahrenheit

"""
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
frase = "-"
print(f"\n{frase*50}\nFunção para converter Celsius para Fahrenheit\n{frase*50}")
celsius_para_fahrenheit(26) 