import requests
import os

os.mkdir("data")

def FetchandSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


url = "https://www.cam.ac.uk/research/news/exhausted-immune-cells-in-healthy-women-could-be-target-for-breast-cancer-prevention"

"""
#  r = requests.get(url) - this means that r is the variable that is storing the url of the url variable. The requests modulue asks for the url by using the method 'get' 
"""

FetchandSaveToFile(url, "data/cam.html")