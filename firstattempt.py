# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:25:27 2020

@author: Clayton
"""
import heapq
import requests
from bs4 import BeautifulSoup
from osrsbox import items_api
items = items_api.load()
bestItems = []
counter = 0
for item in items:
    counter +=1
    if counter % 100 == 0:
        print("item number:",counter)
    if item.highalch == None or item.buy_limit == None:
        continue;
    elif item.highalch > 10000 and item.buy_limit > 10:
        if item.wiki_exchange != None:
            url = str(item.wiki_exchange)
            page = requests.get(url)
            soup = BeautifulSoup(page.content,'html.parser')
            price = soup.find(id='GEPrice')
            intprice = ''.join(x for x in str(price) if x.isdigit())
            if item.highalch-int(intprice) > 0:
                heapq.heappush(bestItems,[(item.highalch-int(intprice))/int(intprice),item.name,item.buy_limit,int(intprice)])

for item in bestItems:
    print(item,"\n")

"""
    
    ItemProperties(id=24944, name='Sourhog foot', incomplete=False, 
                   members=True, tradeable=False, tradeable_on_ge=False, 
                   stackable=False, stacked=None, noted=False, noteable=False, 
                   linked_id_item=None, linked_id_noted=None, 
                   linked_id_placeholder=None, placeholder=False, 
                   equipable=False, equipable_by_player=False, 
                   equipable_weapon=False, cost=1, lowalch=None, highalch=None,
                   weight=0.001, buy_limit=None, quest_item=True, 
                   release_date='2020-09-10', duplicate=False, 
                   examine='A dripping sourhog foot.', 
                   icon='iVBORw0KGgoAAAANSUhEUgAAACQAAAAgCAYAAAB6kdqOAAAB40lEQVR4Xs3XwWrCQBAG4OSYgwcPQgkIQUKQIBJECQalojRQaUsFaaH00Pd/iamzYXYnm41gk1078EMOJvs5OxvU86yWD+1xXj6U4QPsL9k8jCAbDiEdDiAeBBAGgWuUD/PIg/cohOM4lKh8pFD4mSyKXKF8WMUefE4iicJuEQq7dRfQTzIRqPNkLFHYLUQ5B22mngiivuMKhd0ilEOQwuTTy/bEKmk0kHEEUhgCmVA48Eno2T5pdQwH6SgEUYcsdek6hqNw2J1j2kCYu2BMIOyOZQyWGfSvMBzET5blY96OIRB/71jsTvXTgRbGE2MKYeIwELHUHR+Oh6LWCROEY8KRwvQMqjCv5RZOz7urmDaQ/sQOpTDlbi2C120Yy6A6Bq8JRNc6xuL8NDE67LBdyVgEVSdpMZ/L8PnBxU0gnh5/ZtQhmFWWSQyBaJZ0CGZXLCSk4wnzxeIYgmDWy6WAnF/2NZAOIQyGQzpjeBCD2eQ5fLw9CRBiTSDCcJC+yg1VB3EI5etUym3UQRzTK4ggHPNYFCJ8rmZp2orhKH2VG0v/q6vCu8dBHLBezi5fIJP3dJgfVXwQq4c1Z4tA0yQRAMTQoHNIZ0yzmhgC8VnCd1KvXbleze0zxWJXmqVvY1v0+/5avwX903SwF0sLAAAAAElFTkSuQmCC',
                   wiki_name='Sourhog foot', 
                   wiki_url='https://oldschool.runescape.wiki/w/Sourhog_foot', 
                   wiki_exchange=None, equipment=None, weapon=None)
"""