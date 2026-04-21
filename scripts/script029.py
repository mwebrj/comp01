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
-     29. Criar um programa para ler dois números que representam a altura e o peso
de uma pessoa, imprima o índice de massa corporal. IMC = peso / (altura * altura)

"""
altura = float(input("Digite a altura da pessoa (em metros - 1.83) "))
peso = float(input("Digite o peso da pessoa (em kg): "))
imc = peso / (altura * altura)
print(f"O índice de massa corporal (IMC) é: {imc:.2f}")