import requests
from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd
# import time
from fake_useragent import UserAgent
UserAgent().chrome


page_link = ('https://ipoteka.raiffeisen.ru/promo/special/?utm_'
             'source=google&utm_medium=cpc&utm_campaign=ohm|pr:'
             'ml|sp:secondary|plt:search|sem:brand|tg:ssa|city:'
             'st_petersburg|&utm_term=cid-1420670395,agi-'
             '59516043527,adi-358463497602,tid-kwd-298352863821'
             ',dev-c,reg-1012040&utm_content=pview-1t1&gclid='
             'CjwKCAjwtuLrBRAlEiwAPVcZBn_lpkfObJuoZAvepmre4zsJM1'
             'IL-vO3SJEn9jPNKqCR8p2MkayxPxoCBUQQAvD_BwE')
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
html = response.content
print(html[:10000])
soup = BeautifulSoup(html, 'lxml')



# print(response.text)
