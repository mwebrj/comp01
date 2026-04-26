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
-	90. Crie um programa que receba uma frase e troque: A → 4, E → 3, L → 1, T → 7, O → 0, G → 9, S → 5, Z → 2
"""
def main():
    frase = input("Digite uma frase: ")
    frase = frase.replace("A" or "a", "4")
    frase = frase.replace("E" or "e", "3")
    frase = frase.replace("L" or "l", "1")
    frase = frase.replace("T" or "t", "7")
    frase = frase.replace("O" or "o", "0")
    frase = frase.replace("G" or "g", "9")
    frase = frase.replace("S" or "s", "5")
    frase = frase.replace("Z" or "z", "2")
    print(frase)
if __name__ == "__main__":
    main()
    