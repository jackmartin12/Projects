#!/usr/bin/env python
# coding: utf-8

# Jack Martin
# 
# I399, Spring 2021
# 
# Independent Data Project, Part 2

# Overview: Counties in the United States are given a NCHS urbanization code based on their population. Lagest to smallest classes: Large Central Metro, Large fringe metro, medium metro, small metro, micropolitan, and non-core.
# 
# #### Alpha = .01 for all 3 hypothesis
# 
# Below is each hypothesis with the tests following it.
# 
# ### Hypothesis #1
# 
# H0: The differences between the confirmed COVID-19 cases per 100,000 of a "Large central metro" county and the confirmed COVID-19 cases per 100,000 of a "Small metro" county are due to random chance.
# 
# H1: The differences between the confirmed COVID-19 cases per 100,000 of a "Large central metro" county and the confirmed COVID-19 cases per 100,000 of a "Small metro" county are not due to random chance alone.

# In[16]:


import pandas as pd, numpy as np, seaborn as sns

#read in the data
data = pd.read_csv("1_county_level_confirmed_cases.csv")

data.head()


# In[17]:



#find the mean of the cases per 100,000 of a Large Central Metro
lcm = np.mean(data[data['NCHS_urbanization']=='Large central metro']['confirmed_per_100000'])

#find the mean of the cases per 100,000 of a small metro 
sm = np.mean(data[data['NCHS_urbanization']=='Small metro']['confirmed_per_100000'])

print("Mean confirmed cases per 100,000 for 'Large central metro' counties:", lcm)
print("Mean confirmed cases per 100,000 for 'Small metro' counties::",sm)
print()

#get the difference which is our sample statistic
statistic = sm - lcm
print("Our sample statisic is:", statistic)


# In[18]:


#create function
def simulate():
    
    global data
    
    #shuffle the NCHS urbanuzation column
    nchs_shuffle = np.random.permutation(data['NCHS_urbanization'])
    
    data['NCHS Shuffled'] = nchs_shuffle
    
    #getting the confirmed cases per 100,000 from data, where the NCHS class is a Large central Metro
    mean_lcm = np.mean(data[data['NCHS Shuffled']=='Large central metro']['confirmed_per_100000'])
    
       
    #getting the confirmed cases per 100,000 from data, where the NCHS class is a Small Metro
    mean_sm = np.mean(data[data['NCHS Shuffled']=='Small metro']['confirmed_per_100000'])
    
    return mean_sm - mean_lcm


# In[19]:


sims = []

#run the function 10,000 times
for i in range(10000):
    sims.append(simulate())

#what proportion of the sims yield a difference in averages >= the test statistic
sims = np.array(sims)
print("Our p-value is",len(sims[sims >= statistic])/10000)

sns.histplot(sims)


# ### Conclusion #1
# 
# Since our p-value is higher than our aplha value of .01, we accept the null hypothesis. The differences between the confirmed COVID-19 cases per 100,000 of a "Large central metro" county and the confirmed COVID-19 cases per 100,000 of a "Small metro" county are due to random chance.

# ### Hypothesis #2
# 
# H0: The differences between the confirmed COVID-19 Deaths per 100,000 of a "Large central metro" county and the confirmed COVID-19 Deaths per 100,000 of a "Small metro" county are due to random chance.
# 
# H1: The differences between the confirmed COVID-19 Deaths per 100,000 of a "Large central metro" county and the confirmed COVID-19 Deaths per 100,000 of a "Small metro" county are not due to random chance alone.

# In[20]:


#find the mean of the deaths per 100,000 of a Large Central Metro
lcm = np.mean(data[data['NCHS_urbanization']=='Large central metro']['deaths_per_100000'])

#find the mean of the deaths per 100,000 of a small metro
sm = np.mean(data[data['NCHS_urbanization']=='Small metro']['deaths_per_100000'])

print("Mean confirmed deaths per 100,000 for 'Large central metro' counties:", lcm)
print("Mean confirmed deaths per 100,000 for 'Small metro' counties::",sm)
print()

statistic = sm - lcm
print("Our sample statisic is:", statistic)


# In[21]:


#create function
def simulate2():
    
    global data
    
    #shuffle the NCHS urbanuzation column
    nchs_shuffle = np.random.permutation(data['NCHS_urbanization'])
    
    data['NCHS Shuffled'] = nchs_shuffle
    
    #getting the confirmed deaths per 100,000 from data, where the NCHS class is a Large central Metro
    mean_lcm = np.mean(data[data['NCHS Shuffled']=='Large central metro']['deaths_per_100000'])
    
    #getting the confirmed deaths per 100,000 from data, where the NCHS class is a small metro
    mean_sm = np.mean(data[data['NCHS Shuffled']=='Small metro']['deaths_per_100000'])
    
    return mean_sm - mean_lcm


# In[22]:


sims = []

#run the function 10,000 times
for i in range(10000):
    sims.append(simulate2())

#what proportion of the sims yield a difference in averages >= the test statistic
sims = np.array(sims)
print("Our p-value is",len(sims[sims >= statistic])/10000)

sns.histplot(sims)


# ### Conclusion #1
# 
# Since our p-value is higher than our aplha value of .01, we accept the null hypothesis. The differences between the confirmed COVID-19 Deaths per 100,000 of a "Large central metro" county and the confirmed COVID-19 Deaths per 100,000 of a "Small metro" county are due to random chance.

# ### Hypothesis #3
# 
# H0: The differences between the total COVID-19 Deaths of a "Large central metro" county and the total COVID-19 deaths of a "Non-core" county are due to random chance.
# 
# H1: The differences between the total COVID-19 Deaths of a "Large central metro" county and the total COVID-19 deaths of a "Non-core" county are not due to random chance alone.

# In[23]:


#find the mean of the total deaths of a Large Central Metro
lcm = np.mean(data[data['NCHS_urbanization']=='Large central metro']['deaths'])

#find the mean of the total deaths of a Non-core
nc = np.mean(data[data['NCHS_urbanization']=='Non-core']['deaths'])

print("Mean total deaths for 'Large central metro' counties:", lcm)
print("Mean total deaths for 'Non-core' counties::",nc)
print()

statistic = lcm - nc
print("Our sample statisic is:", statistic)


# In[24]:


#create function
def simulate3():
    
    global data
    
    #shuffle the NCHS urbanuzation column
    nchs_shuffle = np.random.permutation(data['NCHS_urbanization'])
    
    data['NCHS Shuffled'] = nchs_shuffle
    
    #getting the total deaths from data, where the NCHS class is a Large central Metro
    mean_lcm = np.mean(data[data['NCHS Shuffled']=='Large central metro']['deaths'])
    
    #getting the total deaths from data, where the NCHS class is a Non-core
    mean_nc = np.mean(data[data['NCHS Shuffled']=='Non-core']['deaths'])
    
    return mean_lcm - mean_nc


# In[26]:


sims = []

#run simulation 10,000 times
for i in range(10000):
    sims.append(simulate3())

#what proportion of the sims yield a difference in averages >= the test statistic
sims = np.array(sims)
print("Our p-value is",len(sims[sims >= statistic])/10000)

sns.histplot(sims)


# ### Conclusion #3
# 
# Our p-value is very small, but it is not 0 according to the histogram above. Since our p-value is smaller than our alpha value of .01, we reject our null hypothesis. The differences between the total COVID-19 Deaths of a "Large central metro" county and the total COVID-19 deaths of a "Non-core" county are not due to random chance alone.

# In[ ]:




