
# coding: utf-8

# # HW Week2
# 

# In[6]:

# The usual preamble - be sure to execute this cell
get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:

pd.__version__


# ## Part 1: Filtering and Counting Things
# 
# Most of the homework questions require you to do simple pandas operations on your data.  It might be a line or two or three.  It is not your goal to write functions, as in previous homework, but to find the commands in pandas that will get you the answers. And SHOW THEM IN THE NOTEBOOK.  This means execute your code and show the answer before you submit your homework file.

# In[7]:

df = pd.read_csv('data/chicago_crimes.csv', parse_dates=['Date-Time'], dayfirst=False,)


# In[8]:

df.describe()


# The problem above is that some of those columns have numbers, but not measures you can do math on. The Beat, District, Ward, Community Area, and id are codes, so you can't take their mean, avg, max etc...  We should change them to string types, of "object" in pandas type notation.

# In[9]:

df = df.astype({"Ward":"object","Beat":"object", "District":"object", "identification":"object", "Community Area": "object"}, copy=True)


# In[5]:

# we can live with these being numbers
df.describe()


# In[28]:

df.head()


# In[52]:

# What are the columns in this data set?
df.columns


# In[ ]:

# Q1: what are all the Primary Types?  Hint: use unique


# In[ ]:

# Q2: Find out how many of each type occur.


# In[ ]:

# Q3: Make a bar chart of the top 10 primary types.


# In[ ]:

# Q4: Make a new dataframe of just the theft types.


# In[ ]:

# Q5: Get the counts of each Description type inside the Thefts dataframe. 


# In[ ]:

# Q6: Using your answer above, make a bar chart of the Description type counts.


# In[ ]:

# Q7: What percentage of all crimes in this data occur in Ward 42? Hint: just find out how many occur in ward 42 and then divide by all crimes.


# In[ ]:

# Q8: What is the most common crime Primary Type that results in an arrest?


# ## Part 2: Stats

# In[1]:

# load in the paris rainfall data - use the 'clean' one.


# In[16]:

rain = pd.read_csv('data/paris_rain_clean.csv', index_col='Year')  # there is one year per row, it can be our index


# In[17]:

rain.describe()


# In[19]:

rain.tail()


# In[112]:

# Q8: use .loc to get all the rain values for the year 1700


# In[ ]:

# Q9: Sort by rain amount in January, ascending=False. Now get the top row. What's the year?


# In[133]:

# Q10: find the values for the month of June. Plot in a bar chart. (It's ok if you can't read the x axis labels.)


# In[ ]:

# Q11: What are the max and min values for Jun?  What is the median?


# In[207]:

# Q12: Make a histogram for one month's rain.


# In[213]:

# Q13: create a column for the total rain each year.  It's okay if you have a NaN for years with columns with missing data, too.


# In[ ]:

# Q14: Plot the proportion or percentage of rain for each January out of the total (hint: jan/total), using a line chart.

