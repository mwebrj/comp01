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
-     33. Criar um programa para ler um número e imprimir quantos bits são necessários para representar o número lido

"""
# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Calcula o número de bits necessários para representar o número
if numero == 0:
    bits_necessarios = 1
else:
    bits_necessarios = numero.bit_length()

# Imprime o resultado
print(f"O número {numero} requer {bits_necessarios} bits para ser representado.")