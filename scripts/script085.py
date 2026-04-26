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
-	85. Crie uma função que receba uma frase digitada pelo usuário e imprima a frase com as palavras em ordem inversa 
"""
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
# Solicitar ao usuário que digite uma frase
user_input = input("Digite uma frase: ")
# Chamar a função para inverter a frase e imprimir o resultado
print("Frase invertida:", reverse_sentence(user_input))
