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
- 4. Criar um programa que recebe uma String e um número e imprime a String lida a quantidade de vezes indicada pelo número lido

"""

mensagem = input("Informe a mensagem: ")
num = int(input("Informe a quantidade de mensagens: "))

for i in range(num):
    print(f"{i+1:2} - {mensagem}")