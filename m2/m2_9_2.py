from bs4 import BeautifulSoup
import requests
import csv
import requests

# r = requests.get('https://www.indiainfoline.com/api/papi-call-api.php?url=/Derivative/Derivative.svc/FNO-Rollover/FUTSTK/?responsetype=json').json()

html_text = requests.get("https://coinmarketcap.com/").text
soup = BeautifulSoup(html_text, "lxml")

f = open("currencies.csv", "w")
writer = csv.writer(f)
header = ["name", "price, $", "Circulating Supply"]
data = []
var = []

table = soup.find("tbody")
trs = table.find_all("tr")

for index, tr in enumerate(trs[0:10]):
    name = tr.find("p", class_="sc-e225a64a-0 ePTNty").text
    price_div = tr.find("div", class_="sc-7510a17-0 hEduBL")
    price = price_div.find("span").text.replace(",", "").replace("$", "")
    supply = tr.find("p", class_="sc-e225a64a-0 gLNGkf")  #
    supply = supply.find("span", class_="sc-b2299d0c-1 hHzHwP").text.replace(",", "")
    more_info = tr.a["href"]
    more_info = "https://coinmarketcap.com" + more_info
    var.append(name)
    var.append(price)
    var.append(supply)
    data.append(var)
    var = []
    print(more_info)
    print(f"Currency Name: {name}")
    print(f"Price $: {price}")
    print(f"Circulating Supply: {supply}")
writer.writerows(data)
