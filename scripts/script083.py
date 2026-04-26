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
-	83. Crie uma função que receba dois números, o primeiro indica a quantidade de zeros 
a esquerda deve ser impressa, e o segundo um número inteiro para ser formatado. 
Imprima o número com a quantidade de zeros a esquerda solicitada.
"""
def formatar_com_zeros(qtd_zeros, numero):
    numero_formatado = str(numero).zfill(qtd_zeros + len(str(numero)))
    return numero_formatado
qtd_zeros = int(input("Digite a quantidade de zeros à esquerda: "))
numero = int(input("Digite o número a ser formatado: "))
print(formatar_com_zeros(qtd_zeros, numero))