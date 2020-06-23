import requests 
from bs4 import BeautifulSoup 
import urllib.request
import random 

url = "https://www.pornpics.com/?q=dani+daniels"

source_code = requests.get(url)

plain_text = source_code.text
print(plain_text)

# soup = BeautifulSoup(plain_text)

# for link in soup.find_all("a",{"class":"rel-link"}):
#     # href = link.get('href')
#     # print(href) 
#     inner_url=link.get('href')
#     source_code1 = requests.get(inner_url)
#     plain_text1 = source_code.text
#     soup1=BeautifulSoup(plain_text1)
#     for link1 in soup1.find_all("a",{"class":'rel-link'}):
#         img_name = random.randrange(1,500)
#         full_name = str(img_name)+ ".jpg"
#         href=link1.find('img')
#         shref=href.get('data-src')
#         print(shref)
#         # urllib.request.urlretrieve(shref, full_name)
#     print("loop break")
