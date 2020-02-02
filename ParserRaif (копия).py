import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
UserAgent().chrome


def get_html(url):
    r = requests.get(url, headers={'User-Agent': UserAgent().chrome})
    print(r.text)
    return r.text


def write_csv(data):
    with open('csvs/Raif.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data(html):

    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find('div', class_='sc-fcdeBU kjeINJ')
    print(all_data)

    all_data1 = all_data.find_all('li', class_='sc-clNaTc gxsYyf')
    all_data2 = all_data.find_all('div', class_='sc-jXQZqI jzvdvL')[0:4]
    datas = all_data1 + all_data2

    for need_data in datas:
        try:
            items = need_data.text.strip()
        except IndexError:
            items = ''

        data = [items]
        print(data)
        # write_csv(data)


def main():
        # ('https://ipoteka.raiffeisen.ru/promo/special/?utm_'
        #  'source=google&utm_medium=cpc&utm_campaign=ohm|pr:'
        #  'ml|sp:secondary|plt:search|sem:brand|tg:ssa|city:'
        #  'st_petersburg|&utm_term=cid-1420670395,agi-'
        #  '59516043527,adi-358463497602,tid-kwd-298352863821'
        #  ',dev-c,reg-1012040&utm_content=pview-1t1&gclid='
        #  'CjwKCAjwtuLrBRAlEiwAPVcZBn_lpkfObJuoZAvepmre4zsJM1'
        #  'IL-vO3SJEn9jPNKqCR8p2MkayxPxoCBUQQAvD_BwE')
    url = ('https://ipoteka.raiffeisen.ru/promo/special/?utm_source'
           '=google&utm_medium=cpc&utm_campaign=ohm|pr:ml|sp:secondary'
           '|plt:search|sem:brand|tg:ssa|city:st_petersburg|&utm_term'
           '=cid-1420670395,agi-59516043527,adi-358463497608,tid-aud'
           '-364736081936:kwd-331763337580,dev-c,reg-1012040&utm_content'
           '=pview-1t2&gclid=Cj0KCQjw_absBRD1ARIsAO4_D3u-MkzMnIdhW2Xe'
           'BaErUF5jNNm-9V3rna1WoRagOTO2wSX0Nv3ELh4aAveeEALw_wcB')

    get_html(url)


if __name__ == '__main__':
    main()
