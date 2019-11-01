
import requests
import bs4
from bs4 import BeautifulSoup
import xlsxwriter

__author__="Bamidele Ojomo"

request =requests.get('https://lccimembership.com/directory')
content=request.content
soup=bs4.BeautifulSoup(content,"html.parser")
tr=soup.find("tr")
get_headers=tr.text.strip()
td=soup.find_all('td',attrs={'class':"body-item mbr-fonts-style display-7"})

b=get_headers.split()
# print(b)
workbook = xlsxwriter.Workbook('lcc.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1',b[0])
worksheet.write('B1',b[1])
worksheet.write('C1',b[2])
worksheet.write('D1',b[3])
worksheet.write('E1',b[4])
worksheet.write('F1',b[5])
worksheet.write('G1',b[6])
worksheet.write('H1',b[7])
worksheet.write('I1',b[8])
worksheet.write('J1',b[9])
worksheet.write('K1',b[10])


for abc in td:
    # print(abc)
    k=abc.text.strip()
    h=k.split()
    print(h)
    # print(k)

# workbook.close()




# element=soup.find("span",{"itemprop":"price","class":"non-price"})

# string_price=element.text.strip()
# price_without_symbol=string_price[1:]
# price=float(price_without_symbol)
# if price <200:
#     print("You should buy the chair")
#     print("The currnet price is {}.".format(string_price))
# else:
#
#     print("Do not buy, it's too expensive!")

# def return_sth():
#     print(dir(BeautifulSoup))
#
#
# if __name__ == '__main__':
#     return_sth()

