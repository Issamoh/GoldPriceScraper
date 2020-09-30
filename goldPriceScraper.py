import sys
import requests
from bs4 import BeautifulSoup
#extracting gold price
url1 = "https://www.kitco.com/gold-price-today-usa/"
page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.content,'html.parser')
results1 = soup1.find(class_="table-price--body-table--overview-detail")
tabelrows = results1.find_all('tr')
for id, tr in enumerate(tabelrows):
    if id==2:
        infos = tr.find_all('td')
        break
#at this stage: infos is a set that contains a title, price in USD, change compared to the last update
infos_list = list(infos)
#converting USD to the currency that we want:
if len(sys.argv)-1 == 0:
    currency = input("Please enter a correct symbol of currency (dzd for example) :")
else:
     currency = sys.argv[1]
url2 ="https://transferwise.com/fr/currency-converter/usd-to-"+currency+"-rate"
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.content,'html.parser')
span = soup2.find('span',class_="text-success")
money = float(span.text.replace(',','.'))
print(money)
#final step:
s = infos_list[0].text+': '+infos_list[1].text+'$'+' ('+'{} '+currency+')'+'  Change from the lase update: '+infos_list[2].text
print(s.format(money*float(infos_list[1].text)))
