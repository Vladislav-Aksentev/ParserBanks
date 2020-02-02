import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/RosSelhozbank.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['items'], data['requirements']))

    with open('csvs/RosSelhozbank.csv') as f:
        writer = f.read().strip('\n')


def write_csv2(data):
    with open('csvs/RosSelhozbank.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data_RosSelhozbank(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find('div', class_='b-tabbed-pages'
                         '').find('div', id='tab20727').find_all('tr')[1:6]

    rate1 = soup.find_all('div', class_='col-md-6')[0].find('big').text
    rate = ['Процентная ставка от'] + [rate1]

    write_csv2(rate)

    for need_data in all_data:
        try:
            items = need_data.find('th').text.strip()
        except IndexError:
            items = ''

        try:
            requirements1 = need_data.find('td').text.strip().strip('\r')
            requirements = requirements1.strip('\n')
        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def main():
    url_RosSelhozbank = ('https://www.rshb.ru/natural/loans/mortgage/')
    get_data_RosSelhozbank(get_html(url_RosSelhozbank))


if __name__ == '__main__':
    main()
