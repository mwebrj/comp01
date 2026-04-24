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
-          60. Crie uma função (def) que receba um número float indicando uma temperatura em Fahrenheit e imprima seu valor em Kelvin

"""
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5.0/9.0 + 273.15
    print(f"{fahrenheit}°F é igual a {kelvin} K")

# Exemplo de uso
fahrenheit_to_kelvin(98.6)
