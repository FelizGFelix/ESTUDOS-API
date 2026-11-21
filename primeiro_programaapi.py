import requests
from pprint import pprint
import os

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def retorno():
    print("-----------------------")
    input("Digite qualquer valor para voltar: ")
    limpar()

def main():
    nome = ""
    
    while True:
        nome = input("Digite o seu nome para pesquisar no site do IBGE: ")

        url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

        resposta = requests.get(url)

        try:
            resposta.raise_for_status()

        except requests.HTTPError as e:
            print(f"erro no request: {e}")
            resultado = None

        else:
            resultado = resposta.json()

        pprint(resultado[0]['res'])
        retorno()

if __name__ == "__main__":
    main()