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
-     23. Criar um programa para ler dois números e se o segundo for diferente 
de zero imprimir a divisão, se for igual a zero imprimir uma mensagem indicando erro.

"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num2 != 0:
    divisao = num1 / num2
    print(f"A divisão do primeiro número {num1} pelo segundo número {num2} é igual a {divisao}.")
else:
    print("Erro: O segundo número é igual a zero. A divisão por zero não é permitida no número real.")