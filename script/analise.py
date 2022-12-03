import pandas as pd
import os

#Variável global
path_input_file = "input/Salaries.csv"
path_output = "output"

# modo de manipular arquivos em python
# "w" escrita
# "r" leitura
# "a" append adicionar

# Criar função para analisar respostas com arquivo txt
def gravar_respostas(path:str, filename:str ,string:str , modo:str = "w", encoding:str = "utf-8"):
    # with abre uma condição até que se encerre os comandos dentro
    # do bloco with
    """
    Função utilizado para gravar texto em um arquivo txt
    Args:
        path (str): caminho do diretório
        filename (str): nome do arquivo
        string (str): texto a para ser criado
        modo (str, optional): modo de manipulação do arquivo. Defaults to "w".
    """
    filename_path = os.path.join(path,filename)

    with open(filename_path, modo, encoding=encoding) as file:
        file.write(string)


# Padrão iniciar a solução a chamada das funções dessa forma 
# com if __name__ == "__main__":

if __name__ == "__main__":
    # Criando cabeçalho para o arquivo de resposta 
    # \n quebra de linha
    string =  "Resposta dos Exercícios\n\nAutor: Pedro\n\n"
    filename = "Resposta.tx"
    gravar_respostas(path_output, filename, string)

    # Carregar base de dados
    df = pd.read_csv(path_input_file, delimiter = ",")
    df.head(10)
    df.info()
    df.describe()


    # tratar base de dados

    # Ex1- Quais colunas tem nesta base?
    string =  "Resposta Ex1:\n"
    # gravando cabeçalho da questão
    gravar_respostas(path_output, filename, string, modo = "a")
    for col in df.columns:
        string = "\t"+col+"\n"
        gravar_respostas(path_output, filename, string, modo = "a")


    # 2

    # 3

    # 4

    # 5

    # 6

    # 7

    # 8

    # 9

    # 10
