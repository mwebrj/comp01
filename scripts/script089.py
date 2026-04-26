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
-	89. Crie um programa que receba uma frase e troque as consoantes para maiúsculas
"""
def convert_consonants_to_uppercase(frase):
    resultado = ""
    for char in frase:
        if char.lower() in "bcdfghjklmnpqrstvwxyz":
            resultado += char.upper()
        else:
            resultado += char
    return resultado
# Solicitar ao usuário que digite uma frase
user_input = input("Digite uma frase: ")
# Imprimir a frase com as consoantes em maiúsculas
print("Frase com consoantes em maiúsculas:", convert_consonants_to_uppercase(user_input))
