import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/Sberbank.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['items'], data['requirements']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='kit-row terms-description__row')

    for need_data in all_data:
        try:
            items = need_data.find('div', class_='kit-text kit-text'
                                   '_s kit-text_note terms-description__'
                                   'text').text.strip("\u200b").strip()

        except IndexError:
            items = ''

        try:
            requirements = need_data.find('div', class_='kit-text kit-text_s '
                                          'terms-description__'
                                          'text').text.strip()

        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def main():
    url = ('https://www.sberbank.ru/ru/person/'
           'credits/home/buying_project?tab=usl')
    get_data(get_html(url))


if __name__ == '__main__':
    main()
