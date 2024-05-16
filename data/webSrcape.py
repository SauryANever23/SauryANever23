import requests
from bs4 import BeautifulSoup


url = "https://wikileaks.org/+-Global-Economy-+.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

titles = soup.select("h2.title")
for title in titles:
    print(title.string)

images = soup.select("img.spip_logos")
for image in images:
    print(image['src'])