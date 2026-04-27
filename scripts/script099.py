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
-	99. Crie um programa que leia números inteiros até que o usuário digite “fim” e 
imprima os fatores primos de cada número que for lido
"""
def main():
    while True:
        user_input = input("Digite um número inteiro (ou 'fim' para encerrar): ")
        if user_input.lower() == "fim":
            break
        
        try:
            number = int(user_input)
            fatores = prime_factors(number)
            print(f"Fatores primos de {number}: {fatores}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

def prime_factors(n):
    fatores = []
    # Verificar fatores de 2
    while n % 2 == 0:
        fatores.append(2)
        n //= 2
    
    # Verificar fatores ímpares a partir de 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fatores.append(i)
            n //= i
    
    # Se n for um número primo maior que 2
    if n > 2:
        fatores.append(n)
    
    return fatores

if __name__ == "__main__":
    main()