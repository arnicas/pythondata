
# coding: utf-8

# # Week 1: Homework Problems
# 
# ** Create your own functions and use the ones we made during the class to answer to the questions** 

# ### Homework Question 1:
# 
# 
# Write the function called "get_lowest", and make it similar to get_highest() in the Review notebook. It should take the same arguments, the data set variable and the column number. Show it working with the column index for Low in data set goog.csv.
# 
# Hint: set the initial value of your variable to float("inf"), which is infinity.
# 
# Your answer to q1:----------------------
#     

# In[1]:

# fix this so it does as required above
def get_lowest():
    # fill this in
    return something


# ### Homework Question 2:
# 
# 
# Now write a function that calculates the difference between the day's open and close stock price, and return the difference. (NOT PRINT. RETURN.) Name your function "get_difference". It should take as argument a row of the dataset. In other words, this is a function that can be called from a function that processes the data in a file like goog.csv.  But you do not have to write that function.
# 
# Hint: A row means mydata[3] (or whatever your data variable is called, or any other index), for instance!

# In[ ]:

def get_difference(row):
    #fill this in
    return difference


# ## Homework Question 3
# 
# You need to use tuples for this one.
# 
# Rewrite your get_lowest function to return a tuple with the date of the lowest, as well as the closing value on that date. Name your function "get_lowest_with_date". It should take 2 arguments, the dataset and the column number for the lowest.
# 
# 
# Your answer to q3:------------------------

# In[ ]:




# In[3]:

def get_lowest_with_date(data, column):
    #fill this in
    return something


# ## Homework 4
# 
# Write a function called "get_volume_data" that takes the data dictionary and returns a new dictionary of just the dates and closing volume values, if it's there.  The dates will be the keys.
# 
# 
# Your answer to q4:-------------------------
#     

# In[4]:

def get_volume_data(dictionary):
    # fill in
    return newdict


# In[ ]:

#show it running -- this should execute without an error:
volumedict = get_volume_data(dictdata)


# In[ ]:

# this should also execute without error and show an item from the dict:
list(volumedict.items())[0]


# In[ ]:



