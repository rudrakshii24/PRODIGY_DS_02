#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data = pd.read_csv(r"C:\Users\rudra\Downloads\titanic\test.csv")
data.head()


# In[6]:


data.describe()


# In[7]:


data.info()


# In[8]:


data.isnull().sum()


# In[9]:


data.dropna(subset=["Embarked"], inplace=True)
data["Cabin"].fillna("Unknown", inplace=True)
data["Age"].fillna(data["Age"].mean(), inplace=True)


# In[10]:


data.isnull().sum()


# In[11]:


data.duplicated().sum()


# In[12]:


plt.figure(figsize=(6, 3))
sns.histplot(data["Age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


# In[18]:


plt.figure(figsize=(6, 3))
sns.countplot(data=data, x="Sex", hue="Ticket")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", loc="upper right")
plt.show()


# In[16]:


plt.figure(figsize=(6, 3))
sns.scatterplot(data=data, x="Age", y="Fare", hue="Ticket")
plt.title("Scatter Plot of Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title="Ticket")
plt.show()


# In[ ]:




