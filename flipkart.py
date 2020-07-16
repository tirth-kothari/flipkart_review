# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:42:43 2020

@author: sumit
"""

import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/intel-q8400-2-66-ghz-lga-775-socket-4-cores-desktop-processor/product-reviews/itmd2ryszb8hztr2?pid=PSREYYGPTSYB9T2M&lid=LSTPSREYYGPTSYB9T2MBZJOLV&marketplace=FLIPKART"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

results=soup.find(id='container')
print(results.prettify())


    
l=[]
rew_elems=results.find_all('div',class_='_3gijNv col-12-12')

for rew_elem in rew_elems:
    print(rew_elem, end='\n'*2)
for rew_elem in rew_elems:
    s=[]
    rew_rate =rew_elem.find('div',class_='row')
    rew_title=rew_elem.find('p',class_='_2xg6Ul')
    rew_cont =rew_elem.find('div',class_='qwjRop')
    rew_person=rew_elem.find('p',class_='_3LYOAd _3sxSiS')
    #print(rew_rate)
    #print(rew_title)
    #print(rew_cont)
    #print(rew_person)
    if None in (rew_rate, rew_cont, rew_title, rew_person):
        continue
    #writer.writerow({'review_rate': rew_rate.text, 'rew_cont': rew_cont.text.strip(),'person_name':rew_person.text.strip()})
    s.append(rew_rate.text)
    s.append(rew_cont.text.strip())
    s.append(rew_person.text.strip())
    l.append(s)
    print(rew_rate.text)
    print(rew_cont.text.strip())
    print(rew_person.text.strip())
    print()

import csv

with open('E:/flipkart.csv', 'w', newline='') as csvfile:
    fieldnames = ['review_rate', 'rew_cont','person_name']
   # writer = csv.DictWriter(file, fieldnames=fieldnames)
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fieldnames)
    csvwriter.writerows(l)
    #writer.writeheader()