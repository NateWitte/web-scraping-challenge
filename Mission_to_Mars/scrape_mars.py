#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import BS, splinter, and CDM
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[3]:


#Scrape newest headline and article
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
quotes = soup.find_all('div', class_='content_title')
newest_title=quotes[0].text
quotes = soup.find_all('div', class_='article_teaser_body')
newest_article=quotes[0].text
browser.quit()


# In[4]:


#Get picture of the day, first going to the website
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url='https://spaceimages-mars.com/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[5]:


browser.links.find_by_partial_text('FULL IMAGE').click()


# In[7]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
quotes = soup.find_all('img', class_='fancybox-image')
image_url=quotes[0]['src']
featured_image_url=url+image_url
print(featured_image_url)


# In[7]:


browser.quit()


# In[8]:


#Start Pandas work
url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
comparison_df=tables[0]
comparison_df


# In[9]:


#Fix format
comparison_df=comparison_df.set_index(0)


# In[10]:


comparison_df=comparison_df.rename(columns=comparison_df.iloc[0]).drop(comparison_df.index[0])
comparison_df.index.name=None


# In[11]:


comparison_df


# In[12]:


html_table = comparison_df.to_html()
html_table=html_table.replace('\n', '')
html_table


# In[13]:


#Hemispheres Part
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url='https://marshemispheres.com/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[14]:


testing=soup.find_all('a', class_ = "itemLink product-item")
searchablehrefs=[]
for result in testing:
    if result['href'] not in searchablehrefs:
        searchablehrefs.append(result['href'])
searchablehrefs


# In[ ]:


hemisphere_image_urls=[]
for link in range(0,4):
    browser.visit(url+searchablehrefs[link])
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #Get href
    testing=soup.find_all('a', target = "_blank")
    partial_url=testing[2]['href']
    #Get title
    testing=soup.find_all('h2', class_ = "title")
    title=testing[0].contents[0].split(" Enhanced")[0]
    hemisphere_image_urls.append({"title": title, "img_url": url+partial_url})
hemisphere_image_urls


# In[ ]:


browser.quit()

