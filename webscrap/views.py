from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas as pd


def index(request):
    return render(request, "webscrap/index.html")


def scr(request, price_stock=None):
    # url = 'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
    url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
    page = requests.get(url)
    # soup = BeautifulSoup(page.text, 'lxml')
    soup = BeautifulSoup(page.text, "html.parser")
    price_stock = soup.find_all('bg-quote', class_='value')[0].text
    print(price_stock)
    closing_price_stock = soup.find('td', class_='table__cell u-semi').text
    print(closing_price_stock)
    # lower_range_header_stock = soup.find_all('div', class_='range__header')[7]
    lower_range_tock = soup.find_all('span', class_='primary')[4].text
    print(lower_range_tock)
    upper_range_tock = soup.find_all('span', class_='primary')[5].text
    print(upper_range_tock)

    #tab = pd.DataFrame({'Price Stoooock': price_stock, 'Closing Stock': closing_price_stock,
           #'L_Stock_Range': lower_range_tock, 'U_Stock_range': upper_range_tock})

    return render(request, 'webscrap/scrap.html', {'p_stock': price_stock, 'c_stock': closing_price_stock,
                                                   'l_stock_Range': lower_range_tock,
                                                   'u_stock_range': upper_range_tock})
