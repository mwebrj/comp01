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
-          66. Crie uma função (def) que converta de Km/h para Milhas/h

"""
def kmh_to_mph(kmh):
    mph = kmh * 0.621371
    return mph
# Exemplo de uso
kmh = 80
mph = kmh_to_mph(kmh)
print(f"{kmh} Km/h é igual a {mph:.2f} Milhas/h")
