#!/usr/bin/env python
# coding: utf-8

# In[258]:


from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random


# In[259]:


page = requests.get("https://nur-sultan.hh.kz/search/vacancy?area=160&search_field=name&search_field=company_name&search_field=description&text=python&from=suggest_post&hhtmFrom=vacancy_search_list", headers={'User-Agent': 'Custom'})
page


# In[260]:


soup = bs(page.content)
soup


# In[261]:


soup.find_all(class_='vacancy-serp-item')


# In[262]:


name = [i.text for i in soup.find_all(class_='resume-search-item__name')]
name


# In[263]:


len(name)


# In[264]:


link =[i.find('a').get('href') for i in soup.find_all(class_='resume-search-item__name')]
link


# In[265]:


len(link)


# In[266]:


employer = [i.text for i in soup.find_all(class_='vacancy-serp-item__meta-info-company')]
employer


# In[267]:


description=[]
for url in link:
    page = requests.get(url,headers={'User-Agent': 'Custom'})
    # Getting the webpage's content in pure html
    soup = bs(page.content)
    description.append(",".join([i.text for i in soup.find_all(class_='vacancy-description')]))


# In[268]:


# Creating a DataFrame to store our newly scraped information
df = pd.DataFrame()
# Storing the quotes and authors in their respective columns
df['Name of the job'] = name
df['Description'] = description
df['Employer'] = employer


# In[269]:


df


# In[270]:


df.to_csv('Task1.csv', index=False, encoding='utf-8')

