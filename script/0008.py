# 0008

import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.hao123.com'
data = requests.get(url)
r = re.findall(r'<body>[\s\S]*</body>', data.text)

print('---------------------------------------------------------------')
soup = BeautifulSoup(data.text,'html.parser')
print(soup.body.text)
