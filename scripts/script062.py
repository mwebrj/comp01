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
-          62. Crie uma função (def) que receba um número float indicando uma medida em quilogramas e imprima seu valor em libras

"""
def kilograms_to_pounds(kilograms):
    pounds = kilograms * 2.20462
    print(f"{kilograms} kg é igual a {pounds:.2f} libras")
# Exemplo de uso

kilograms_to_pounds(75)