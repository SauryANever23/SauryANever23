import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=laptops&crid=2WOERC8BUXQLT&sprefix=laptop%2Caps%2C343&ref=nb_sb_noss_1"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# getting titles from the website
span = soup.select("class.a-size-mini a-spacing-none a-color-base s-line-clamp-2")

for spans in span:
    print(spans.string, "\n\n")

print(span, "\n\n")
# scraping price
# prices = soup.select("span.a-price-whole")

# for price in prices:
#     print(price.string, "\n\n")