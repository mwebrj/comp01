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
-	88. Ler uma String e imprimir se a frase é um palíndromo
"""
def is_palindrome(frase):
    frase = frase.replace(" ", "").lower()  # Remover espaços e converter para minúsculas
    return frase == frase[::-1]  # Verificar se a frase é igual à sua inversa
# Solicitar ao usuário que digite uma frase
user_input = input("Digite uma frase: ")
# radar, rotor, rvivr, mirim, arara, osso, ovo, asa, anilina...
# A cara rajada da jararaca
# Seco de raiva, coloco no colo caviar e doces
# Verificar se a frase é um palíndromo e imprimir o resultado
if is_palindrome(user_input):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
