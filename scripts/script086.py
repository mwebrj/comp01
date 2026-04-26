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
-	86. Crie uma função que receba uma frase e imprima as palavras na ordem certa mas com as letras em ordem inversa
"""
def print_words_reverse_order(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    frase_invertida = ' '.join(palavras_invertidas)
    print(frase_invertida)
# Solicitar ao usuário que digite uma frase
frase_usuario = input("Digite uma frase: ")
# Chamar a função para imprimir as palavras com as letras em ordem inversa
print_words_reverse_order(frase_usuario)