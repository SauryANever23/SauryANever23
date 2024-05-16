import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=laptop&crid=3K3RQ3DZ80PCB&sprefix=laptop%2Caps%2C250&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())