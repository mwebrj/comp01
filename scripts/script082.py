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
-	82. Strings (elaborar um script dizendo a quantidade de caracteres de um nome de pessoa)
"""
nome = input("Digite o nome de uma pessoa: ")
quantidade_caracteres = len(nome)
print("Espaços contam como um caractere...")
print(f"O nome '{nome}' tem {quantidade_caracteres} caracteres.")