import requests
from bs4 import BeautifulSoup as Soup
import secrets
import sys
sys.dont_write_bytecode = True

def get_language_listing():
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
    language_listing = get_language_listing()
    results = ' '.join(secrets.choice(language_listing) for i in range(3))
    print(results)

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))