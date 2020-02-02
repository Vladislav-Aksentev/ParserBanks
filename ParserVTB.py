import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/VTB.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='padding-slim '
                             'common-text')[2].find_all('li')[0:5]

    for need_data in all_data:
        try:
            items = need_data.text
        except IndexError:
            items = ''

        data = [items]
        write_csv(data)


def main():
    url = ('https://www.vtb.ru/personal/ipoteka/novostrojki/#calc_0#')
    get_data(get_html(url))


if __name__ == '__main__':
    main()
