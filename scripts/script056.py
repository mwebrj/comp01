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
-      56. Criar um programa para ler uma String que representa uma data de nascimento do usuário e imprimir a idade atual em anos, meses e dias.

"""

from datetime import datetime
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
data_atual = datetime.now()
idade_anos = data_atual.year - data_nascimento.year
idade_meses = data_atual.month - data_nascimento.month
idade_dias = data_atual.day - data_nascimento.day
if idade_dias < 0:
    idade_meses -= 1
    idade_dias += 30
    
print(f"Anos: {idade_anos}")
print(f"Meses: {idade_meses}")
print(f"Dias: {idade_dias}")

