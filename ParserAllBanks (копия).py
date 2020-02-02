import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('csvs/AllBanks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['items'], data['requirements']))


def write_csv2(data):
    with open('csvs/AllBanks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def write_csv_name_firs_bank(bank):
    with open('csvs/AllBanks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(bank)
        writer.writerow('\n')


def write_csv_name_next_bank(bank):
    with open('csvs/AllBanks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow('\n')
        writer.writerow(bank)
        writer.writerow('\n')


def get_data_Sber(html):

    bank = ['Sberbank']
    write_csv_name_firs_bank(bank)

    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='kit-row terms-description__row')

    for need_data in all_data:
        try:
            items = need_data.find('div', class_='kit-text kit-text_s '
                                   'kit-text_note '
                                   'terms-description__'
                                   'text').text.strip("\u200b").strip()
        except IndexError:
            items = ''
        try:
            requirements = need_data.find('div', class_='kit-text'
                                          ' kit-text_s terms-description_'
                                          '_text').text.strip()
        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def get_data_Spb(html):

    bank = ['SPB']
    write_csv_name_next_bank(bank)

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


def get_data_VTB(html):

    bank = ['VTB']
    write_csv_name_next_bank(bank)

    soup = BeautifulSoup(html, 'lxml')
    all_data = soup.find_all('div', class_='padding-slim '
                             'common-text')[2].find_all('li')[0:5]

    for need_data in all_data:
        try:
            items = need_data.text
        except IndexError:
            items = ''

        data = [items]
        write_csv2(data)


def get_data_UralSib(html):

    bank = ['UralSib']
    write_csv_name_next_bank(bank)

    soup = BeautifulSoup(html, 'lxml')
    all_data1 = soup.find_all('div', class_='row')[2]
    all_data = all_data1.find_all('li', class_='list__item')

    for need_data in all_data:
        try:
            items = need_data.text
        except IndexError:
            items = ''

        data = [items]
        write_csv2(data)


def get_data_Rosbank(html):

    bank = ['Rosbank']
    write_csv_name_next_bank(bank)

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


def get_data_Akbars(html):

    bank = ['Akbars']
    write_csv_name_next_bank(bank)

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


def get_data_Absolut(html):

    bank = ['Absolut']
    write_csv_name_next_bank(bank)

    soup = BeautifulSoup(html, 'lxml')
    all_data2 = soup.find('main', class_='main')
    all_data1 = all_data2.find_all('ul', class_='list list-flex layout-'
                                   'highlights-horizontal')[1]
    all_data = all_data1.find_all('div', class_='highlight-text')

    rate1 = all_data2.find('div', class_='number-value').text.strip()
    rate = ['Процентная ставка от ' + str(rate1)]
    write_csv2(rate)

    for need_data in all_data:
        try:
            items = need_data.text.strip()
        except IndexError:
            items = ''

        data = [items]
        write_csv2(data)


def get_data_Raif(html):

    bank = ['Raif']
    write_csv_name_next_bank(bank)

    file_Raif = open('Ипотека в Райффайзенбанке_ вторичное жилье, '
                     'новостройки, рефинансирование.html').read()
    soup = BeautifulSoup(file_Raif, 'lxml')
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
        write_csv2(data)


def get_data_RosSelhozbank(html):

    bank = ['RosSelhozbank']
    write_csv_name_next_bank(bank)

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
            requirements = need_data.find('td').text.strip()
        except IndexError:
            requirements = ''

        data = {'items': items, 'requirements': requirements}
        write_csv(data)


def main():
    url_Sber = ('https://www.sberbank.ru/ru/person'
                '/credits/home/buying_project?tab=usl')
    get_data_Sber(get_html(url_Sber))

    url_Spb = ('https://www.bspb.ru/retail/mortgage/first/standart/')
    get_data_Spb(get_html(url_Spb))

    url_VTB = ('https://www.vtb.ru/personal/ipoteka/novostrojki/#calc_0#')
    get_data_VTB(get_html(url_VTB))

    url_UralSib = ('https://www.uralsib.ru/promo/reshaytes-na-bolshee?utm_'
                   'source=google_ipoteka&utm_medium=cpc&utm_content=astat'
                   ':kwd-298352867661|ret:kwd-298352867661|cid:6445632932|'
                   'gid:78421651833|aid:377201450819|pos:1t1|st:|src:|dvc:'
                   'c|reg:1012040&utm_campaign=us_ga_reg_s_ipoteka_brand&u'
                   'tm_term=%2B%D1%83%D1%80%D0%B0%D0%BB%D1%81%D0%B8%D0%B1%'
                   '20%2B%D0%B8%D0%BF%D0%BE%D1%82%D0%B5%D0%BA%D0%B0|mt:b&g'
                   'clid=CjwKCAjwq4fsBRBnEiwANTahcOUT6c6svyct_9ee9ch34TXG7'
                   '7ELUQfNYnr9Z3h4qhviP0hgfb2eWhoCT-EQAvD_BwE')
    get_data_UralSib(get_html(url_UralSib))

    url_Rosbsnk = ('https://www.rosbank.ru/ipoteka/novostrojka/')
    get_data_Rosbank(get_html(url_Rosbsnk))

    url_Akbars = ('https://www.akbars.ru/individuals/hypothec/perspektiva/')
    get_data_Akbars(get_html(url_Akbars))

    url_Absolut = ('https://absolutbank.ru/personal/loans/mortgage/'
                   'new-buildings/#')
    get_data_Absolut(get_html(url_Absolut))

    file_Raif = open('Ипотека в Райффайзенбанке_ вторичное жилье, '
                     'новостройки, рефинансирование.html').read()
    get_data_Raif(file_Raif)

    url_RosSelhozbank = ('https://www.rshb.ru/natural/loans/mortgage/')
    get_data_RosSelhozbank(get_html(url_RosSelhozbank))


if __name__ == '__main__':
    main()
