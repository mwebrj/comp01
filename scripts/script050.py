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
-     50. Criar um programa para ler 1 número e imprimir todos os números primos entre ele e 10 * o número

"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Digite um número: "))
    if num < 0:
        print("Número inválido. Digite um número não negativo.")
        return
    print(f"Números primos entre {num} e {10 * num}:")
    for i in range(num, 10 * num + 1):
        if is_prime(i):
            print(i)
if __name__ == "__main__":
    main()
    