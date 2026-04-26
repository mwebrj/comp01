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
-	93. Crie um programa que percorre um arquivo-texto linha a linha e caso encontre 
uma certa String fornecida pelo usuário copie a linha para outro arquivo
"""
def copiar_linha_com_string(arquivo_origem, arquivo_destino, string_procurada):
    with open(arquivo_origem, 'r') as origem, open(arquivo_destino, 'w') as destino:
        for linha in origem:
            if string_procurada in linha:
                destino.write(linha)
                
arquivo_origem = "texto.txt"
arquivo_destino = "linhas_copiadas.txt"
string_procurada = input("Informe a string procurada: ")

copiar_linha_com_string(arquivo_origem, arquivo_destino, string_procurada)

with open(arquivo_destino, "r") as f:
    print(f.read())