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
-          68. Crie uma função (def) que converta de Coordenadas Cartesianas para Coordenadas Polares       

"""
import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta
# Exemplo de uso
x = 2
y = 2
r, theta = cartesian_to_polar(x, y)
print(f"Coordenadas Cartesianas: ({x}, {y})")
print(f"Coordenadas Polares: (r={r:.2f}, θ={theta:.2f} radianos)")
