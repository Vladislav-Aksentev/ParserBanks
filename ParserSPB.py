import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/SPB.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['items'], data['requirements']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find('tbody').find_all('tr')

    for need_data in all_data:
        try:
            items = need_data.find('big').find('strong').text.strip()
        except IndexError:
            items = ''

        try:
            requirements = need_data.find_all('big')[1].text
        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def main():
    url = 'https://www.bspb.ru/retail/mortgage/first/standart/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
