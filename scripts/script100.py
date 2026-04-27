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
-	100. Crie um programa que sorteie 50 números de 0 a 200, imprima a média dos números
e indique o maior e o menor número sorteado
"""
import random

numbers = [random.randint(0, 200) for _ in range(50)]
average = sum(numbers) / len(numbers)
max_number = max(numbers)
min_number = min(numbers)

print(f"Números sorteados: {numbers}")
print(f"Média dos números: {average}")
print(f"Maior número sorteado: {max_number}")
print(f"Menor número sorteado: {min_number}")
