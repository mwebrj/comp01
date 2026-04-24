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
-          61. Crie uma função (def) que receba um número float indicando uma medida em polegadas e imprima seu valor em centímetros

"""
def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    print(f"{inches} polegadas é igual a {centimeters} centímetros")
# Exemplo de uso
inches_to_centimeters(10)
