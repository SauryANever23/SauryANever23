import requests
from bs4 import BeautifulSoup
import wget
import os

import shutil

url = "https://wikileaks.org/+-Global-Economy-+.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

titles = soup.select("h2.title")
for title in titles:
    print(title.string)

# images = soup.select("img.spip_logos")
images = soup.find_all('img')
# print(images1)
# for image in images:
#     print(image['src'])

# List to store image URLs
image_urls = []

# Extract the 'src' attribute from each <img> tag
for img in images:
    img_src = img.get('src')
    if img_src:
        # Optionally, resolve the URL if it's relative
        img_url = requests.compat.urljoin(url, img_src)
        image_urls.append(img_url)

# Print the list of image URLs
for img_url in image_urls:
    print(img_url)


for i in range(len(image_urls)):
    wget.download(image_urls[i])
  
    

