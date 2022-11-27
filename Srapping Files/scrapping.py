import string

from bs4 import BeautifulSoup
import requests

# getting Html from Website

url = 'https://www.webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup.prettify())

# All tags
header = soup.header
# print(header)
# specific tag access
p_tag = soup.header.p.string
print(p_tag)
# after .string function
print(p_tag.string)

# Attributes
attribute = soup.header.a.attrs
print(attribute)
# access specific attribute value in the tag
data_toggle = attribute['data-target-2']
print(data_toggle)
# single line code man header tag se specifc tag ki specifc value access ki.
c= soup.header.a['data-target']
print(c)