import requests 
from bs4 import BeautifulSoup 
import urllib.request
import random 
import string
import os
i=0
first=input("enter the first name")
last=input("enter the last name ")
print(first,last)
url = "https://www.pornpics.com/?q="+str(first.lower())+"+"+str(last.lower())
print(url)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)
name=soup.find('h1').text
name=name.replace("Pics","")
name=name.strip()
for link in soup.find_all("a",{"class":"rel-link"}):
 inner_url=link.get('href')
 # print(inner_url)
 source_code1 = requests.get(inner_url)
 plain_text1 = source_code1.text
 soup1=BeautifulSoup(plain_text1)
 for link1 in soup1.find_all("a",{"class":'rel-link'}):
     img_name = i
     name_star = name+str(img_name)+ ".jpg"
     href=link1.find('img')
     shref=href.get('src')
     urllib.request.urlretrieve(shref, name_star)
     i+=1
 print("loop break")
