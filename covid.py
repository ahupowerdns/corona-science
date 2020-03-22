#!/usr/bin/env python
# coding: utf-8

# In[144]:


get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('precision', '3')

from IPython.display import set_matplotlib_formats
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [9.5, 5]

import pandas


# In[194]:


data=pandas.read_csv("/home/ahu/Downloads/Jelmer Vissers's Coronavirus in Nederland per gemeente (weekend update door bert hubert) - Gemeenten_alfabetisch_2019(1).csv")
data = data[data.Provincienaam != "Nvt"]
data= data[data.Provincienaam.notnull()]
data.head()


# In[195]:


north=["Noord-Holland", "Zuid-Holland", "Drenthe", "Flevoland", "Gelderland", "Groningen", "Friesland", "Utrecht", "Overijssel"]
south=["Limburg", "Noord-Brabant", "Zeeland"]


# In[196]:


days=range(1,23)
arr={'day': [], 'count':[], 'province':[]}
for prov in data["Provincienaam"].unique():
    zh=data[data["Provincienaam"]==prov]
    for a in days:
        s="{0:0=2d}".format(a)
        arr["day"].append(a)
        arr["count"].append(pandas.to_numeric(zh["COVID "+s+"-03"]).sum())
        arr["province"].append(prov)


# In[197]:


zh=data[data["Provincienaam"].isin(north)]
for a in days:
        s="{0:0=2d}".format(a)
        arr["day"].append(a)
        arr["count"].append(pandas.to_numeric(zh["COVID "+s+"-03"]).sum())
        arr["province"].append("north")

zh=data[data["Provincienaam"].isin(south)]    
for a in days:
        s="{0:0=2d}".format(a)
        arr["day"].append(a)
        arr["count"].append(pandas.to_numeric(zh["COVID "+s+"-03"]).sum())
        arr["province"].append("south")
        
df = pandas.DataFrame(data=arr)
df.sort_values("count", inplace=True)


# In[198]:


plt.figure()
for prov in data["Provincienaam"].unique():
    sel=df[df.province==prov].rolling(3).mean()
    plt.plot(sel.day, 100.0*sel["count"].diff()/sel["count"], label=prov)
    
plt.grid()
plt.xlabel("Day in March")
plt.ylabel("3-day smoothed growth percentage")
plt.title("Smoothed daily growth rate for the Dutch provinces")
plt.ylim(0,100)
plt.legend(loc=2)


# In[206]:


plt.figure()

for prov in ["north", "south"]:
    #print(df[df.province==prov].sort_values("day"))
    sel=df[df.province==prov].sort_values("day").rolling(2).mean()
    plt.plot(sel.day, 100.0*sel["count"].diff()/sel["count"], label=prov)
  
plt.grid()
plt.xlabel("Day in March")
plt.ylabel("2-day smoothed growth percentage")
plt.ylim(0)
plt.xlim(0, 30)
plt.legend()
plt.title("Daily growth COVID-19 pos. tests for north/south (NB, Zeeland, Limburg) of The Netherlands, 22nd of March")


# In[200]:


plt.figure()

for prov in ["north", "south"]:
    #print(df[df.province==prov].sort_values("day"))
    sel=df[df.province==prov].sort_values("day").rolling(2).mean()
    plt.plot(sel.day, sel["count"], label=prov)
  
plt.grid()
plt.xlabel("Day in March")
plt.ylabel("2-day smoothed number")
plt.ylim(0)
plt.legend()
plt.title("COVID-19+ tests for the north and the south (NB, Zeeland, Limburg) of The Netherlands")


# In[201]:


plt.figure()

for prov in [ "north", "south"]:
    #print(df[df.province==prov].sort_values("day"))
    sel=df[df.province==prov].sort_values("day")
    plt.plot(sel.day, sel["count"], label=prov)
  
plt.grid()
plt.xlabel("Day in March")
plt.ylabel("Absolute number")
plt.yscale("log")
plt.legend()
plt.title("COVID-19+ tests for the north and the south (NB, Zeeland, Limburg) of The Netherlands")


# In[140]:


df[(~df.province.isin(north)) & (~df.province.isin(south)) & (df.province != "north") & (df.province != "south")]

