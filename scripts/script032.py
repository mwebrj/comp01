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
-     32. Criar um programa para ler dois números que representam dois anos, 
imprimir quantos e quais são os anos bissextos entre os dois anos indicados

"""
# Leitura dos anos
ano1 = int(input("Digite o primeiro ano: "))
ano2 = int(input("Digite o segundo ano: "))

# Determinar o menor e o maior ano
menor_ano = min(ano1, ano2)
maior_ano = max(ano1, ano2)

# Encontrar os anos bissextos
anos_bissextos = []
for ano in range(menor_ano, maior_ano + 1):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        anos_bissextos.append(ano)

# Imprimir os resultados
print(f"Quantidade de anos bissextos entre {menor_ano} e {maior_ano}: {len(anos_bissextos)}")
print(f"Anos bissextos: {anos_bissextos}")