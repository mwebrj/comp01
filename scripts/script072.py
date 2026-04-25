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
-          72. Criar um programa para imprimir o maior número de uma lista

"""
def maior_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
# Exemplo de uso
numeros = [12, 14, 4, 2, 33, 55]
resultado = maior_numero(numeros)
print("O maior número da lista é:", resultado)
