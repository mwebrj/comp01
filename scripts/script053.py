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
-     53. Criar um programa que procure números “amigos”

"""
def soma_de_divisores(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def os_amigos(num1, num2):
    return soma_de_divisores(num1) == num2 and soma_de_divisores(num2) == num1
def encontrar_amigos(limit):
    amigos = []
    for i in range(1, limit):
        for j in range(i + 1, limit):
            if os_amigos(i, j):
                amigos.append((i, j))
    return amigos
limit = 2000
os_amigos = encontrar_amigos(limit)
print(f"Amigos encontrados até {limit}:")
for par in os_amigos:
    print(par)
