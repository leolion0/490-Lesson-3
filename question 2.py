import numpy as np
import requests
from bs4 import BeautifulSoup

html = requests.get("http://en.wikipedia.org/wiki/Supervised_learning")
# wikiPage = open("deeplearning.html", "w")
# wikiPage.write(html.text)
# wikiPage.close()
soup = BeautifulSoup(html.content, "html.parser")

print(soup.title.string)
for i in soup.find_all("a"):
    print(i.get("href"))
# f = open("output.txt", "w")
# f.write(soup.prettify())
# f.close()
