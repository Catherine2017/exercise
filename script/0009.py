# 0009
import requests
from bs4 import BeautifulSoup

url = "http://www.hao123.com"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
urls = soup.findAll("a")
for u in urls:
    print(u['href'])
