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
-	81. Crie um programa que receba do usuário um número indicando a quantidade de 
notas a processar, em seguida crie uma lista de float para armazenar as notas dos
alunos, e, por fim, imprimir as notas em ordem crescente ordenando a lista utilizando
a técnica bubble sort

"""
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
quantidade = int(input("Digite a quantidade de notas a processar: "))
notas = []
for _ in range(quantidade):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
notas_ordenadas = bubble_sort(notas)
print("Notas em ordem crescente:")
for nota in notas_ordenadas:
    print(nota)
