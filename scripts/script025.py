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
-     25. Criar um programa para ler um número que representa um ano e indicar se é
um ano bissexto. (Se o ano for divisível por 400 ou se for divisível por 4 
e não por 100)

"""
ano = int(input("Digite um ano: "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")