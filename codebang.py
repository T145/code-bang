import requests
from bs4 import BeautifulSoup as Soup
from random import choices
import sys
sys.dont_write_bytecode = True


# TODO: Add check for count being <= 25
def get_benfrederickson_langs(count):
    resp = requests.get(
        'https://www.benfrederickson.com/ranking-programming-languages-by-github-users/')
    page = Soup(resp.text, features='html.parser')
    table = page.find('table').find('tbody')('tr')
    listings = [row('td')[1].text.strip() for row in table]
    return choices(listings, k=count)


def get_wikipedia_langs(count):
    resp = requests.get(
        'https://en.wikipedia.org/wiki/List_of_programming_languages')
    page = Soup(resp.text, features='html.parser')
    listings = list()

    for section in page.body('div', attrs={'class': 'div-col columns column-width'}):
        for listing in section('li'):
            listings.append(listing.a.text.strip())

    return choices(listings, k=count)


def main(av, ac):
    for i, lang in enumerate(get_wikipedia_langs(5)):
        print('{}. {}'.format(i+1, lang))


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
