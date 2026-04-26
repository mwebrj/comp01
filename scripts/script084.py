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
-	84. Crie uma função que receba várias Strings até que o usuário digite “fim” e imprima
o tamanho da String, quantas e quais vogais contém, qual a posição da primeira vogal, 
quantas palavras formam a frase.
"""
def analisar_string():
    while True:
        string = input("Digite uma string (ou 'fim' para encerrar): ")
        if string.lower() == "fim":
            break
        
        tamanho = len(string)
        vogais = "aeiouAEIOU"
        vogais_encontradas = [letra for letra in string if letra in vogais]
        quantidade_vogais = len(vogais_encontradas)
        posicao_primeira_vogal = next((i for i, letra in enumerate(string) if letra in vogais), None)
        quantidade_palavras = len(string.split())
        
        print("-" * 40)
        print(f"Tamanho da String: {tamanho}")
        print(f"Quantidade de vogais: {quantidade_vogais}")
        print(f"Vogais encontradas: {', '.join(set(vogais_encontradas))}")
        print(f"Posição da primeira vogal: {posicao_primeira_vogal}")
        print(f"Quantidade de palavras: {quantidade_palavras}")
        print("-" * 40)
# Chamar a função para iniciar o processo
analisar_string()
