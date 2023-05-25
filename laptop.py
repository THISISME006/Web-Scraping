#!/usr/bin/env python
# coding: utf-8
##
# In[2]:


pip install pandas


# In[3]:


import bs4


# In[4]:


from bs4 import BeautifulSoup
import requests
import csv 
import pandas as p


# In[34]:


laptop_name=[]
laptop_price=[]
laptop_rating=[]
page_num=input("Enter number of pages")
for i in range(1,int(page_num)+1):
    url="https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=0c0a7006-f00f-4a2a-831b-d45f547933ad&page="+str(i)
    req=requests.get(url)
    content=BeautifulSoup(req.content,'html.parser')
    name=content.find_all('div',{'class':'_4rR01T'})
    price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
    rating=content.find_all('div',{'class':'_3LWZlK'})
    print("Laptop in page " +str(i))
    print(len(name))
    for i in name:
        laptop_name.append(i.text)
    for i in price:
        laptop_price.append(i.text)
    for i in rating:
        laptop_rating.append(i.text)
        


# In[26]:


for i in laptop_name:
    print(i)


# In[27]:


for i in laptop_price:
    print(i)


# In[36]:


for i in laptop_rating:
    print(i)


# In[45]:


data={"Laptop name":laptop_name,"Laptop price":laptop_price}
d=p.DataFrame(data)
print(d)


# In[42]:


d.to_csv('fk_data_laptop.csv')


# In[ ]:





# In[ ]:




