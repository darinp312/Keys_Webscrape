from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.native-instruments.com/en/catalog/komplete/keys/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

synth_items = html_soup.find_all('div', class_="product-box css-fu9fw6")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Name, Price \n'

f.write(headers)

for synth in synth_items:
    name = synth.find('h2', class_="product-tile-title css-190bron").text
    price = synth.find('span', class_="product-tile-original-price").text

    f.write(name + ',' + price + '\n')

f.close()
