import requests
from bs4 import BeautifulSoup
import csv


def get_html_Rosbank(url):
    r = requests.get(url)
    return r.text


def write_csv2(data):
    with open('csvs/Rosbank.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data1 = soup.find_all('ul')[10].find_all('li')[1:6]
    all_data2 = soup.find_all('p')[6:7]
    all_data = all_data1 + all_data2

    for need_data in all_data:
        try:
            items = need_data.text
        except IndexError:
            items = ''

        data = [items]
        write_csv2(data)


def main():
    url_Rosbsnk = ('https://www.rosbank.ru/ipoteka/novostrojka/')
    get_data(get_html_Rosbank(url_Rosbsnk))


if __name__ == '__main__':
    main()
