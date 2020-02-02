import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv_Absolut(data):
    with open('csvs/Absolut.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data_Absolut(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data1 = soup.find('main', class_='main')
    all_data_first1 = all_data1.find('div', class_='subhero-row-item')
    all_data_first = all_data_first1.find_all('div', class_='number-value')

    all_data_second1 = all_data1.find_all('ul', class_='list list-flex layout-'
                                          'highlights-horizontal')[1]
    all_data_second = all_data_second1.find_all('div', class_='highlight-text')

    all_data = all_data_first + all_data_second

    for need_data in all_data:
        try:
            items = need_data.text.strip()
        except IndexError:
            items = ''

        data = [items]
        print(data)
        # write_csv_Absolut(data)


def main():
    url_Absolut = ('https://absolutbank.ru/personal/loans/mortgage/'
                   'new-buildings/#')
    get_data_Absolut(get_html(url_Absolut))


if __name__ == '__main__':
    main()
