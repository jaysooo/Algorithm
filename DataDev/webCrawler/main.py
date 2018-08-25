#-*- coding: euc-kr -*-
import requests
import re
from bs4 import BeautifulSoup

#req=requests.get("https://beomi.github.io/beomi.github.io_old/")
req=requests.get("http://finance.naver.com")
html=req.text
soup=BeautifulSoup(html,"html.parser")

titles=soup.find_all('a')
#print(titles)

for elem in titles:
    print(elem.text)
