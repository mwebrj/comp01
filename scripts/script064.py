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
-          64. Crie uma função (def) que converta de KgF para Newtons

"""
def kgf_to_newtons(kgf):
    newtons = kgf * 9.80665
    print(f"{kgf} KgF é igual a {newtons:.2f} Newtons")

# Exemplo de uso
kgf_to_newtons(20)