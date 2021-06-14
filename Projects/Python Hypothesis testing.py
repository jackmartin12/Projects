#!/usr/bin/env python
# coding: utf-8

#  Jack Martin
# 
# I399, Spring 2021
# 
# Weekly Practice 8

# In[3]:


import pandas as pd, numpy as np, seaborn as sns

births = pd.read_csv("baby.csv")


# ### Test Hypotheses:
# 
# H0: The differences between the gestational days of a pregnancy with a maternal smoker and the gestational days of a pregnancy without a maternal smoker are due to random chance.
# 
# H1: The differences between the gestational days of a pregnancy with a maternal smoker and the gestational days of a pregnancy without a maternal smoker are not due to random chance alone.

# In[18]:


smoker = np.mean(births[births['Maternal Smoker']==True]['Gestational Days'])

nonsmoker = np.mean(births[births['Maternal Smoker']==False]['Gestational Days'])

print("Non-smokers:", nonsmoker)
print("smokers:",smoker)
print()

statistic = nonsmoker - smoker
print("Our sample statisic is:", statistic)


# In[19]:


def simulate():
    
    global births
    
    smoke_shuffle = np.random.permutation(births['Maternal Smoker'])
    
    births['Smoker Shuffled'] = smoke_shuffle
    
    #getting the birth weight from births, where births smoker shuffled is true
    mean_smoker = np.mean(births[births['Smoker Shuffled']==True]['Gestational Days'])
    
    mean_nonsmoker = np.mean(births[births['Smoker Shuffled']==False]['Gestational Days'])
    
    return mean_nonsmoker - mean_smoker


# In[23]:


sims = []

for i in range(100000):
    sims.append(simulate())

sims = np.array(sims)
print("Our p-value is",len(sims[sims >= statistic])/100000)

sns.histplot(sims)


# ### Conclusion
# 
# Since our p-value is higher than our alpha value of 0.01, we accept the null hypothesis. The differences between the gestational days of a pregnancy with a maternal smoker and the gestational days of a pregnancy without a maternal smoker are due to random chance.

# ### Test hypotheses #2
# 
# H0: The differences between the maternal pregnancy weight with a maternal smoker and the maternal pregnancy weight without a maternal smoker are due to random chance.
# 
# H1: The differences between the maternal pregnancy weight with a maternal smoker and the maternal pregnancy weight without a maternal smoker are not due to random chance alone.

# In[24]:


smoker_weight = np.mean(births[births['Maternal Smoker']==True]['Maternal Pregnancy Weight'])

nonsmoker_weight = np.mean(births[births['Maternal Smoker']==False]['Maternal Pregnancy Weight'])

print("Non-smokers:", nonsmoker_weight)
print("smokers:",smoker_weight)
print()

statistic2 = nonsmoker_weight - smoker_weight
print("Our sample statisic is:", statistic2)


# In[25]:


def simulate2():
    
    global births
    
    smoke_shuffle = np.random.permutation(births['Maternal Smoker'])
    
    births['Smoker Shuffled'] = smoke_shuffle
    
    #getting the birth weight from births, where births smoker shuffled is true
    mean_smoker = np.mean(births[births['Smoker Shuffled']==True]['Maternal Pregnancy Weight'])
    
    mean_nonsmoker = np.mean(births[births['Smoker Shuffled']==False]['Maternal Pregnancy Weight'])
    
    return mean_nonsmoker - mean_smoker


# In[26]:


sims = []

for i in range(100000):
    sims.append(simulate2())

sims = np.array(sims)
print("Our p-value is",len(sims[sims >= statistic2])/100000)

sns.histplot(sims)


# ### Conclusion
# 
# Since our p-value is higher than our alpha value of 0.01, we accept the null hypothesis. The differences between the maternal pregnancy weight with a maternal smoker and the maternal pregnancy weight without a maternal smoker are due to random chance.

# In[ ]:




