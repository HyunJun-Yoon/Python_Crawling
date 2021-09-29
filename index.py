from bs4 import BeautifulSoup
from urllib.request import urlopen

response= urlopen('https://www.naver.com') 
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.select("span.blind"):
    print(anchor.get_text())