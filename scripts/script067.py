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
-          67. Crie uma função (def) que converta de Dólar para Real

"""
def dollar_to_real(dollar, exchange_rate):
    real = dollar * exchange_rate
    return real
# Exemplo de uso
dollar = 100
exchange_rate = 5.25  # Taxa de câmbio atual
real = dollar_to_real(dollar, exchange_rate)
print(f"{dollar} Dólares é igual a {real:.2f} Reais")
