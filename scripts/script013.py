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
-     13. Criar um programa para ler um número que representa o valor de uma 
conta de restaurante e a quantidade de pessoas, imprimir o valor por pessoa

"""
linha = "-"*70
valor = float(input("Informe o valor da conta: "))
qtd = int(input("Informe a quantidade de clientes: "))
print(linha)
print(f"Quantidade de pessoas: {qtd}\nValor por pessoa: R${valor/qtd:.2f}\t Valor Total: R${valor:.2f}")
print(linha)
