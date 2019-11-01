from requests import get
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing

url = 'https://www.konga.com/product/nokia-1-2018-1gb-8gb-rom-android-8-0-5mp-2mp-blue-3907446'
response = get(url)
# print(response)
# print(response.text)
# print(response.content)
html_soup = BeautifulSoup(response.text, 'html.parser')
konga_site = html_soup.find_all('div', class_ = '_24849_2Ymhg')
h4=html_soup.find("h4")
# print(h4)
get_headers=h4.text.strip()
# print(konga_site)
print(get_headers)
b=get_headers.split()
print(b)

# price_scrap=html_soup.find('input',name='product_price')
# print(price_scrap)
price_price=html_soup.find_all(attrs={'name': 'product_price'})


print(price_price)
for x in price_price:
    print(x['value'])



# html_soup = BeautifulSoup(response.text, 'html.parser')
# # print(html_soup)
# # konga_site = html_soup.find_all('div', class_ = 'aadf4_2-w0o')
# # print(konga_site)
#
# # name_box = html_soup.find('h1, attrs={class'=''})
# name_box = BeautifulSoup.find_all('h4', attrs={'class': 'name'})
# # print name_box
#
# # name = konga_site.text()

