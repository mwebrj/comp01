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
-	97. Crie um programa que leia números float até que o usuário digite “fim” e converta 
o valor lido de centímetros para polegadas
"""

def main():
    while True:
        user_input = input("Digite um número em centímetros (ou 'fim' para encerrar): ")
        if user_input.lower() == "fim":
            print("Sistema finalizado.")
            break
        try:
            cm_value = float(user_input)
            inches_value = cm_value / 2.54
            print(f"{cm_value} cm é igual a {inches_value:.2f} polegadas.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim' para encerrar.")
if __name__ == "__main__":
    main()
