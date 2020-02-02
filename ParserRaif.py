# import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open('csvs/Raif.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data(html):

    file = open('Ипотека в Райффайзенбанке_ вторичное жилье, '
                'новостройки, рефинансирование.html').read()
    soup = BeautifulSoup(file, 'lxml')
    all_data = soup.find('div', class_='sc-fcdeBU kjeINJ')
    all_data1 = all_data.find_all('li', class_='sc-clNaTc gxsYyf')
    all_data2 = all_data.find_all('div', class_='sc-jXQZqI jzvdvL')[0:4]
    datas = all_data1 + all_data2

    for need_data in datas:
        try:
            items = need_data.text.strip()
        except IndexError:
            items = ''

        data = [items]
        write_csv(data)


def main():
    file = open('Ипотека в Райффайзенбанке_ вторичное жилье, '
                'новостройки, рефинансирование.html').read()
    get_data(file)


if __name__ == '__main__':
    main()
