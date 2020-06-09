import requests
from bs4 import BeautifulSoup as Soup
import secrets
import sys
sys.dont_write_bytecode = True

def get_wikipedia_langs():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_programming_languages')
    page = Soup(resp.text, features='html.parser')
    headings = page.body('div', attrs={'class': 'div-col columns column-width'})
    langs = list()

    # There will likely be some language sanitization required, like w/ Viper for example

    for heading in headings:
        for child in heading('li'):
            langs.append(child.a.text)
    
    return langs

def main(av, ac):
    langs = get_wikipedia_langs()
    results = [secrets.choice(langs) for i in range(5)]

    for i, result in enumerate(results):
        print('{}. {}'.format(i+1, result))

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))