from bs4 import BeautifulSoup
import logging
import json

import requests

import collections.abc
#hyper needs the four following aliases to be done manually.
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

from hyper.contrib import HTTP20Adapter
logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')



product = input("input year: ")

s = requests.Session()
s.mount('https://', HTTP20Adapter())

def evil(session,num):
    links_container = []
    ref = "https://ru.wikipedia.org/wiki/"
    url = ref + num + "_%D0%B3%D0%BE%D0%B4"


    request = session.get(url)

    bs = BeautifulSoup(request.text, "html.parser")

    all_link = bs.find_all("ul", id="")
    for link in all_link:
        links_container.append( link)
    
    resus = []
    flag = False
    for ek in links_container[2]:
        flag = "1.1" in ek.text
        if "\n" in ek.text:
            continue
        resus.append(ek.text)
        if(flag):
            break

    if flag :
        resus = []
        for ek in links_container[3]:
            if "\n" in ek.text:
                continue
            resus.append(ek.text)
    
    return resus
    

resus = evil(s, product)
for i in resus:
    print(i)
    
dict_hist = []

for year in range(2023):
    dict_hist.append(evil(s, str(year)))
    logger.info(f'{year} добавлен')

dict_for_json = {}
for i in range(1,2023):
    dict_for_json[i] = dict_hist[i]

#2j_dict = json.dump(dict_for_json)



with open("events.txt", "w") as file:
    json.dump(dict_for_json, file)

hui = {}
with open("events.txt", "r") as f:
    hui = json.load(f)

print(hui)