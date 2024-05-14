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



# for child in soup.find(class_="ucontainer").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent)
#     break

# count = soup.find(class_="container")
# count.name = "span"
# count["class"] = ""
# print(count)



#* ul = soup.new_tag("ul")
#*li = soup.new_tag("li")
#* li.string = "helol"
#* ul.append(li)

#* li = soup.new_tag("li")
#* li.string = "about"
#* ul.append(li)

#* soup.html.body.insert(0, ul)
#* with open("modified.html", "w") as f:
#*    f.write(str(soup))


# cont = soup.find(class_="container")
# print(cont.has_attr('class'))

def has_class_no_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

reult = soup.find_all(has_content)
print(reult)
results = soup.find_all(has_class_no_id)
