from bs4 import BeautifulSoup
import requests

#url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)
# required Tag
price_stock = soup.find_all('bg-quote', class_='value')[0].text
print(price_stock)

closing_price_stock = soup.find('td', class_='table__cell u-semi').text
print(closing_price_stock)

# lower_range_header_stock = soup.find_all('div', class_='range__header')[7]
lower_range_tock = soup.find_all('span', class_='primary')[4].text
print(lower_range_tock)

upper_range_tock = soup.find_all('span', class_='primary')[5].text
print(upper_range_tock)

import pandas as pd

table = pd.DataFrame(
    {'Price Stock': [price_stock], 'Closing Stock': [closing_price_stock],
     'Lower Stock Range': [lower_range_tock], 'Upper Stock range': [upper_range_tock]}).to_html()
print(table)
