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
-     27. Criar um programa para ler um número e imprimir a tabuada de 0 a 10 daquele número

"""

# Ler um número do usuário
numero = int(input("Digite um número para ver a tabuada: "))
# Imprimir a tabuada de 0 a 10
print(f"Tabuada de {numero}:")
for i in range(11):
    print(f"{numero} x {i} = {numero * i}")
    