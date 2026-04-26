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
-	92. Crie um programa que recebe dois nomes de arquivo e copia o conteúdo do primeiro (txt) para o segundo
"""
def copiar_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r') as origem:
            conteudo = origem.read()
        
        with open(arquivo_destino, 'w') as destino:
            destino.write(conteudo)
        
        print(f"Conteúdo do arquivo '{arquivo_origem}' copiado para '{arquivo_destino}' com sucesso.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
def main():
    arquivo_origem = input("Digite o nome do arquivo de origem (com extensão .txt): ")
    arquivo_destino = input("Digite o nome do arquivo de destino (com extensão .txt): ")
    copiar_arquivo(arquivo_origem, arquivo_destino)
if __name__ == "__main__":
    main()
    