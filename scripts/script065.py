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
-          65. Crie uma função (def) que converta de m3 para litros

"""
def cubic_meters_to_liters(cubic_meters):
    liters = cubic_meters * 1000
    print(f"{cubic_meters} m³ é igual a {liters} litros")
# Exemplo de uso
cubic_meters_to_liters(0.027)