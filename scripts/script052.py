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
-     52. Programa que leia números inteiros até que o usuário digite 0 e calcule a soma dos pares, 
a média dos ímpares e liste todos os números primos lidos

"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def main():
    soma_pares = 0
    soma_impares = 0
    contador_impares = 0
    primos = []

    while True:
        numero = int(input("Digite um número inteiro (0 para encerrar): "))
        
        if numero == 0:
            break
        
        if numero % 2 == 0:
            soma_pares += numero
        else:
            soma_impares += numero
            contador_impares += 1
        
        if is_prime(numero):
            primos.append(numero)

    media_impares = soma_impares / contador_impares if contador_impares > 0 else 0

    print(f"Soma dos números pares: {soma_pares}")
    print(f"Média dos números ímpares: {media_impares}")
    print(f"Números primos lidos: {primos}")
if __name__ == "__main__":
    main()
    