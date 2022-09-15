#!/usr/bin/env python
# coding: utf-8

# In[6]:


from time import sleep
from numpy import tensordot
from selenium.common.exceptions import *
from click import NoSuchOption
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


final_data=pd.DataFrame() #Initiating Dataframe to store data
tender_name_list=[]#Initiating List to store respective tender name
Industry_list=[]#Initiating List to store respective industry
Location_of_contract_list=[]#Initiating List to store respective location of contract
Value_of_contract_list=[]#Initiating List to store respective value of contract
Procurement_reference_list=[]#Initiating List to store respective procurment 
Published_date_list=[]#Initiating List to store respective published date
Closing_date_list=[]#Initiating List to store respective closing date
Closing_time_list=[]#Initiating List to store respective clossing time

path = r'geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)

for z in range(1,7):  #Note-Increase the range and we can scrape more data
    try:
        driver.get(f'https://www.contractsfinder.service.gov.uk/Search/Results?page={z}#07c879eb-5e62-435b-8034-10e114ec9938')
        sleep(2) 
        
        for x in range(1,21):
                try:
                    driver.find_element(By.XPATH,f'//div[3]/div/div/div/div[1]/div[{x}]/div[1]/h2/a').click()
                    sleep(2)
                    try:
                        tender_name=driver.find_element(By.XPATH,'//h1[@class="govuk-heading-l break-word"]')
                        tender_name_list.append(tender_name.text)
                    except:
                        tender_name_list.append('tender name missing')

                    try:
                        industry=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/ul/li/p')
                        Industry_list.append(industry.text)
                    except:
                        Industry_list.append('industry missing')

                    try:    
                        location_of_contract=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[2]/span')
                        Location_of_contract_list.append(location_of_contract.text)
                    except:
                        Location_of_contract_list.append('location of contract missing')
                    
                    try:
                        value_of_contract=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[3]')
                        Value_of_contract_list.append(value_of_contract.text)
                    except:
                        Value_of_contract_list.append('value of contract missing')

                    try:
                        procurement_reference=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[4]')
                        Procurement_reference_list.append(procurement_reference.text)
                    except:
                        Procurement_reference_list.append('procurement reference missing')

                    try:
                        published_date=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[5]')
                        Published_date_list.append(published_date.text)
                    except:
                        Published_date_list.append('published date missing')

                    try:
                        closing_date=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[6]')
                        Closing_date_list.append(closing_date.text)
                    except:
                        Closing_date_list.append('closing date missing')
                    
                    try:
                        closing_time=driver.find_element(By.XPATH,'//*[@id="content-holder-left"]/div[3]/p[7]')
                        Closing_time_list.append(closing_time.text)
                    except:
                        Closing_time_list.append('closing time missing')

                        
                except:
                    print('NO DATA RECEIVED')
                driver.back()
                
    except:
        print('INVALID URL')


final_data['Tender name']=tender_name_list
final_data['Industry']=Industry_list
final_data['Location of contract']=Location_of_contract_list
final_data['Value of contract']=Value_of_contract_list
final_data['Procurment references']=Procurement_reference_list
final_data['Published date']=Published_date_list
final_data['closing date']=Closing_date_list
final_data['closing time']=Closing_time_list
final_data.to_csv(r"D:\amazon dataset\richa.csv")


# In[13]:


# importing required libraries
import pandas as pd
import numpy as np


# In[14]:


df = pd.read_csv("richa.csv")
df.head()


# In[15]:


df.shape


# In[16]:


df.info()


# In[17]:


#cleaning
df['Procurment references'] =df['Procurment references'].str.replace("Procurment references","")


# In[18]:


df['Value of contract'] =df['Value of contract'].str.replace("Value of contract","")


# In[19]:


df['Location of contract'] =df['Location of contract'].str.replace("Location of contract","")


# In[21]:


df['closing date'] =df['closing date'].str.replace("closing date","")


# In[22]:


df['closing time'] =df['closing time'].str.replace("closing time","")


# In[23]:


df['Industry'] =df['Industry'].str.replace("Industry","")


# In[26]:


df.describe()


# In[27]:


df['Location of contract'].value_counts()


# In[28]:


#contract values
newdf = df["Value of contract"].str.split(" ", n = 4, expand = True)


# In[29]:


newdf


# In[31]:


#taking highest values
newdf[2]=newdf[2].str.replace("£","")
newdf


# In[33]:


df['Value of contract']=newdf[2]


# In[35]:


df['Value of contract'] =df['Value of contract'].fillna(0)


# In[52]:


df.head()


# In[38]:


import seaborn as sns


# In[53]:


sns.pairplot(df)


# In[50]:


plt.title("Closing year for Recieving Bids")
sns.countplot(x=df['closing date'])


# In[54]:


plt.title("Industry for Recieving Bids")
sns.countplot(x=df['Industry'])


# In[49]:


plt.title("Tender based Location of contract")
sns.countplot(x=df['Location of contract'])


# In[43]:


from matplotlib import pyplot as plt


# In[46]:


plt.title("Location of contract vs Publication year")
sns.countplot(x=df['Location of contract'],hue=df['Published date'])


# In[47]:


from matplotlib.pyplot import figure
figure(figsize=(8, 6), dpi=80)
plt.title("Location of contract vs  closing date")
sns.countplot(x=df['Location of contract'],hue=df['closing date'])


# In[63]:


pip install pygal_maps_world

# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.World()

# set the title of the map
worldmap.title = 'Countries'

# adding the countries
worldmap.add('df['Industry']', df['Location of contract'])

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")

# In[69]:


df.plot(x="Industry", y="Location of contract", kind="scatter", c="red",
        colormap="YlOrRd")


# In[78]:


pip install geopandas


# import matplotlib.pyplot as plt
# import pandas as pd
# from geopandas import gpd
# From GeoPandas, our world map data
worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Creating axes and plotting world map
fig, ax = plt.subplots(figsize=(12, 6))
df.plot(color="lightgrey", ax=ax)

# Plotting our Impact Energy data with a color map
x = df['Location of contract']
y = df['Industry']
z = df['Tender name']
plt.scatter(x, y, s=20*z, c=z, alpha=0.6, vmin=0, vmax=threshold,
            cmap='autumn')
plt.colorbar(label='Tender name')

# Creating axis limits and title
plt.xlim([-180, 180])
plt.ylim([-90, 90])

first_year = df["Published date"].min().strftime("%Y")
last_year = df["closing date"].max().strftime("%Y")
plt.title("contact location with industry" +     
          str(first_year) + " - " + str(last_year))
plt.xlabel("Location of contract")
plt.ylabel("Industry")
plt.show()
# In[ ]:




