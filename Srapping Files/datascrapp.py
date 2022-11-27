import string

from bs4 import BeautifulSoup
import requests

# getting Html from Website

url = 'https://www.webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup)

# find function
header = soup.find('header')
# print(header)
# specific tag 1st give tag name than class name
s_tag = soup.find('h4', {'class': 'pull-right price'})
# another method
p_tag = soup.find('h4', class_='pull-right price')
# print(s_tag)
# print(p_tag)
# اگر ایک پیج پر موجود کسی خاص ٹیگ جو بار بار ہو اُس کے لیے
h4_tag = soup.find_all('h4', class_='pull-right price')
# print(h4_tag)
# agr timam ki bijay koi aik makhsoos tag result lainy ho to wo index location se ho ga
h4_tag = soup.find_all('h4', class_='pull-right price')[5]
# print(h4_tag)

url2 = 'https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page2 = requests.get(url2)
# print(page)
soup2 = BeautifulSoup(page2.text, 'lxml')
# print(soup2)
# aik makhsos price k liya index location ka use
price_tag = soup2.find_all('h4', class_='pull-right price')[14]
# print(price_tag)
# agr aap chahy k makhsoas value k bad ki timam value fetch ho to index mein location k " : " daal kr space day timam onward values fetch ho jian ge
price_tag = soup2.find_all('h4', class_='pull-right price')[14:]
# print(price_tag)
# اگر ایک ہی ٹیگ میں مختلف کلاسز یا ایک وقت میں مختلف ٹیگ کا دیٹا لینا ہو تو
Multi_tag = soup2.find_all(['h4', 'p', 'a'])
# print(Multi_tag)
# Specific name wise data fetch
name_data = soup2.find_all(string='Acer Iconia')
# print(name_data)
# agr kisi name se jo exact na ho search krni ho to but remeber this it is case Sensitive
import re

ran_search = soup2.find_all(string=re.compile('Pad'))
calss_search = soup2.find_all(class_=re.compile('img-responsive'))
# agr kisi aik tag se linked puri web se koi specific class fetch krni ho to aur sath limit k kitny record lainy hai
pull_tag = soup2.find_all('p', class_=re.compile('pull-right'), limit=2)
# print(ran_search)
# print(calss_search)
# print(pull_tag)
# lets do some valueable work
product_name = soup2.find_all('a', class_='title')
#print(product_name)
product_price = soup2.find_all('h4', class_='pull-right price')
# print(product_price)
product_description = soup2.find_all('p', class_='description')
# print(product_description)
product_reviews = soup2.find_all('p', class_='pull-right')
# print(product_reviews)

product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
# print(product_name_list)

product_price_list = []
for i in product_price:
    name = i.text
    product_price_list.append(name)
# print(product_price_list)

product_description_list = []
for i in product_description:
    name = i.text
    product_description_list.append(name)
# print(product_description_list)

product_reviews_list = []
for i in product_reviews:
    name = i.text
    product_reviews_list.append(name)
# print(product_reviews_list)

# ab timam data ko table mein show krny k liya k liya pandas library use
import pandas as pd

table = pd.DataFrame(
    {'Product Name': product_name_list, 'Price': product_price_list, 'Description': product_description_list,
     'Reviews': product_reviews_list}).to_html()
# print(table)
