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
-     51. Programa que leia números inteiros até que o usuário digite 0 e calcule a média dos números

"""
def main():
    soma = 0
    contador = 0

    while True:
        numero = int(input("Digite um número inteiro (0 para encerrar): "))
        
        if numero == 0:
            break
        
        soma += numero
        contador += 1

    if contador > 0:
        media = soma / contador
        print(f"A média dos números digitados é: {media}")
    else:
        print("Nenhum número foi digitado.")
if __name__ == "__main__":
    main()
    