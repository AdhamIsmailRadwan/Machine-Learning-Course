#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as files
import matplotlib.pyplot as plt

location = r'/Users/adhamismail/Downloads/Courses/Machen learing/Data/Data Week3/smoke_detection_iot.csv'

data = files.read_csv(location)

Yes_count = 0
No_count = 0
for i in data["Fire_Alarm"]:
    if i == 1:
        Yes_count +=1
    else:
        No_count+= 1

yescount_Sum_nocount = Yes_count +No_count

percent_of_YesFire = (Yes_count*100)/ yescount_Sum_nocount
print(f"Yes Fire: {percent_of_YesFire}")
percent_of_NoFire = (No_count*100)/ yescount_Sum_nocount
print(f"No Fire: {percent_of_NoFire}")

colors = ['red', 'blue']

fvalues = ['Yes Fire', 'No Fire']
sizes = [percent_of_YesFire, percent_of_NoFire]

fig, ax = plt.subplots()
ax.pie(sizes, labels=fvalues, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Fire Alarm Data')
ax.legend(labels, loc='lower left')

plt.show()


# In[14]:


import pandas as files
import matplotlib.pyplot as plt

location = r'/Users/adhamismail/Downloads/Courses/Machen learing/Data/Data Week3/smoke_detection_iot.csv'

data = files.read_csv(location)

Yes_count = 0
No_count = 0
for i in data["Fire_Alarm"]:
    if i == 1:
        Yes_count +=1
    else:
        No_count+= 1

yescount_Sum_nocount = Yes_count +No_count

percent_of_YesFire = (Yes_count*100)/ yescount_Sum_nocount
print(f"Yes Fire: {percent_of_YesFire}")
percent_of_NoFire = (No_count*100)/ yescount_Sum_nocount
print(f"No Fire: {percent_of_NoFire}")

colors = ['red', 'blue']

fvalues = ['Yes Fire', 'No Fire']
sizes = [percent_of_YesFire, percent_of_NoFire]

fig, ax = plt.subplots()
ax.pie(sizes, labels=fvalues, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Fire Alarm Data')
ax.legend(labels, loc='lower left')

plt.show()


# In[14]:


import pandas as files
import matplotlib.pyplot as plt

location = r'/Users/adhamismail/Downloads/Courses/Machen learing/Data/Data Week3/smoke_detection_iot.csv'

data = files.read_csv(location)

Yes_count = 0
No_count = 0
for i in data["Fire_Alarm"]:
    if i == 1:
        Yes_count +=1
    else:
        No_count+= 1

yescount_Sum_nocount = Yes_count +No_count

percent_of_YesFire = (Yes_count*100)/ yescount_Sum_nocount
print(f"Yes Fire: {percent_of_YesFire}")
percent_of_NoFire = (No_count*100)/ yescount_Sum_nocount
print(f"No Fire: {percent_of_NoFire}")

colors = ['red', 'blue']

fvalues = ['Yes Fire', 'No Fire']
sizes = [percent_of_YesFire, percent_of_NoFire]

fig, ax = plt.subplots()
ax.pie(sizes, labels=fvalues, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Fire Alarm Data')
ax.legend(labels, loc='lower left')

plt.show()


# In[ ]:




