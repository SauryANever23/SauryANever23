import requests
from bs4 import BeautifulSoup




url = "https://www.amazon.in/s?k=laptops&crid=2WOERC8BUXQLT&sprefix=laptop%2Caps%2C343&ref=nb_sb_noss_1"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r = requests.get(url, headers=headers)
# Whenever using BeautifulSoup create a soup object    
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())