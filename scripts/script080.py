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
-	80. Criar um programa para imprimir a soma dos fatores primos de um número dado.

"""
def soma_fatores_primos(n):
    soma = 0
    for i in range(2, n + 1):
        while n % i == 0:
            soma += i
            n //= i
    return soma
numero = int(input("Digite um número: "))
resultado = soma_fatores_primos(numero)
print(f"A soma dos fatores primos de {numero} é: {resultado}")
