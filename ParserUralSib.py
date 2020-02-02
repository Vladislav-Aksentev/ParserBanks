import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open('csvs/UralSib.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_data1 = soup.find_all('div', class_='row')[2]
    all_data = all_data1.find_all('li', class_='list__item')
    for need_data in all_data:
        try:
            items = need_data.text
        except IndexError:
            items = ''

        data = [items]
        write_csv(data)


def main():
    url = ('https://www.uralsib.ru/promo/reshaytes-na-bolshee?utm_source='
           'google_ipoteka&utm_medium=cpc&utm_content=astat:kwd-298352867661|'
           'ret:kwd-298352867661|cid:6445632932|gid:78421651833|aid:377201450'
           '819|pos:1t1|st:|src:|dvc:c|reg:1012040&utm_campaign=us_ga_reg_s_'
           'ipoteka_brand&utm_term=%2B%D1%83%D1%80%D0%B0%D0%BB%D1%81%D0%B8%D0'
           '%B1%20%2B%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BA%D0%B0|mt:b&gclid=Cj'
           'wKCAjwq4fsBRBnEiwANTahcOUT6c6svyct_9ee9ch34TXG77ELUQfNYnr9Z3h4qhv'
           'iP0hgfb2eWhoCT-EQAvD_BwE')
    get_data(get_html(url))


if __name__ == '__main__':
    main()
