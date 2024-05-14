import requests
from bs4 import BeautifulSoup




url = "https://www.amazon.in/s?k=laptops&crid=2WOERC8BUXQLT&sprefix=laptop%2Caps%2C343&ref=nb_sb_noss_1"




r = requests.get(url)
# Whenever using BeautifulSoup create a soup object    
soup = BeautifulSoup(r.text, 'html.parser')


span = soup.find(class_="a-section a-spacing-small a-spacing-top-small")
print(span.)