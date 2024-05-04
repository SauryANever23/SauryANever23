import requests
from bs4 import BeautifulSoup

with open("data/sample.html", "r") as f:
    html_doc = f.read()

# Whenever using BeautifulSoup create a soup object    
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# print(soup.find_all("div")[1])

# a For loop to find the anchor tags in the html file
# for link in soup.find_all("a"):
#     print(link)
#     print(link.getText())
# s = soup.find(id="link3")

# print(s['href'])
# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.p.getText())
# a = soup.find_all(class_="italic")
# print(a)
         
# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)

count = soup.find(class_="container")
count.name = "span"
count["class"] = "ucontainer"
print(count)

