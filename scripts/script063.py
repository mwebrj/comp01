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
-          63. Crie uma função (def) que converta de graus para radianos

"""
import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    print(f"{degrees} graus é igual a {radians:.4f} radianos")
# Exemplo de uso
degrees_to_radians(45)
