import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/Akbars.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['items'], data['requirements']))


def get_data_Akbars(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='v-grid-cell '
                             'v-cell-pc-4 v-cell-pc-columns-3')

    for need_data in all_data:
        try:
            items = need_data.find('span').text.strip()

        except IndexError:
            items = ''

        try:
            requirements = need_data.find('h3').text.strip()

        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def main():
    url_Akbars = ('https://www.akbars.ru/individuals/hypothec/perspektiva/')
    get_data_Akbars(get_html(url_Akbars))


if __name__ == '__main__':
    main()
