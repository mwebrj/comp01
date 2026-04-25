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
-          71. Criar um programa para imprimir o menor número de uma lista

"""
def menor_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor
# Exemplo de uso
numeros = [12, 14, 4, 2, 33, 55]
resultado = menor_numero(numeros)
print("O menor número da lista é:", resultado)