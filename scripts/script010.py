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
-     10. Criar um programa para ler dois números e uma String com um operador e imprimir o resultado da operação

"""

def calculo(a, b, operar):
    match operar:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Erro: Divisão por zero"
        case _:
            return "Operador inválido"
        
while True:
    status = input("Deseja realizar o cálculo? (s, n): ")
    if status == "n":
        print("Saindo do sistema...")
        break
    else:
        num1 = float(input("Informe o primeiro número:"))
        num2 = float(input("Informe o segundo número: "))
        operador = input("Informe o operador (+, -. *, /): ")
        print(calculo(num1, num2, operador))
  



