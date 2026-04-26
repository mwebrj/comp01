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
-	91. Crie um programa que receba uma frase e um int e codifique cada letra somando 
o número recebido ao código. Deve ser possível decodificar uma frase 
(apresentar um menu).
"""

def codificar(frase, num):
    frase_codificada = ""
    for letra in frase:
        if letra.isalpha():
            codigo_letra = ord(letra)
            codigo_letra += num
            frase_codificada += chr(codigo_letra)
        else:
            frase_codificada += letra
    return frase_codificada

def decodificar(frase, num):
    frase_decodificada = ""
    for letra in frase:
        if letra.isalpha():
            codigo_letra = ord(letra)
            codigo_letra -= num
            frase_decodificada += chr(codigo_letra)
        else:
            frase_decodificada += letra
    return frase_decodificada

def main():
    while True:
        print("Menu:")
        print("1. Codificar frase")
        print("2. Decodificar frase")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            frase = input("Digite a frase a ser codificada: ")
            num = int(input("Digite o número para codificar: "))
            frase_codificada = codificar(frase, num)
            print("Frase codificada:", frase_codificada)
        
        elif escolha == "2":
            frase = input("Digite a frase a ser decodificada: ")
            num = int(input("Digite o número para decodificar: "))
            frase_decodificada = decodificar(frase, num)
            print("Frase decodificada:", frase_decodificada)
        
        elif escolha == "3":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
    