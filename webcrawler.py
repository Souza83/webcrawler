import requests  # Requisição http
from bs4 import BeautifulSoup  # Trabalha com html, xml
import operator  # Para operadores +-*/ not and
from collections import Counter  # Manipula listas, tuplas dicionarios


# Função que define o webcrawler que chama a função clean_wordlist
def start(url):

    wordlist = []  # armazena conteúdo do site
    source_code = requests.get(url).text  # faz requisição da url

    soup = BeautifulSoup(source_code, 'html.parser')  # transforma em html

    # Procura tudo que existe com a tag <div> e class no conteúdo
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()  # transforma em letra minúscula

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


# Remove simbolos indesejados e remove com um espaço
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = ' !@#$%^&*()_-+={[}]|\;:<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


# Cria um dicionário e faz contagem e gera um top 20
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Contador de palavras chaves
    for key, value in sorted(word_count.items(),
                             key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
