
# coding: utf-8

# # CSV Data Review, Tuples, Pandas Intro

# At the end of the Python bootcamp, you were analysing csv files.  This is the first step for most data analysis.
# 
# In this lesson, we will add a few more tools to your concepts, including tuples and sets. Then we will briefly introduce the basic tool for data analysis of multi-column datasets in Python, the pandas library.
# 
# First...
# 
# In order to read a file into the notebook, it must be in the same directory (or "folder") as the notebook you are running. You can see what files you have by using "ls":

# In[3]:

ls


# My data is in the folder data, so we can list that and see the files:

# In[5]:

ls data


# Let's load that file into python, using a recommended construction we didn't discuss in the bootcamp, and count the rows while we do that:

# In[2]:

with open("data/goog.csv", errors="ignore") as file:
    rowCounter = 0
    for row in file:
        print(row)
        rowCounter += 1  # add one to the counter for each row


# In[3]:

print("There are", rowCounter, "rows in this data.")


# What are some things we might want to know about this stock data?
# Maybe:
#     
# * highest value
# * lowest value
# * largest volume
# * biggest difference in a single day (high-low)
# 
# You've done some of those things in the bootcamp when you looked for longest and shortest names.  We didn't save the data when we read it in.  We need to assign it to a variable.  I'll make a function to read and return that value.

# In[4]:

def read_data(filename):
    # Function takes file path, and returns a list of the rows of the data
    data = []
    with open(filename, errors="ignore") as file:
        for row in file:
            data.append(row)
    return data


# In[5]:

mydata = read_data("data/goog.csv")


# In[6]:

len(mydata)


# In[7]:

mydata[0]


# In[8]:

# Let's get rid of the first row using a slice operation to skip the first item
mydata = mydata[1:]


# In[9]:

mydata[0]


# In[10]:

len(mydata)


# Now let's make a function to find the highest value.  The question is which value do we check?  Let's just look at the High value.  But to make this general, let's just pass in the index of the column we want to check.  That way it's easy to check other columns!
# 

# In[12]:

def get_highest(data, column):
    highest = 0
    for row in data:
        # we have to split it up by the comma, to use the column index:
        vals = row.split(",")
        if vals[column] > highest:
            highest = vals[column]
    return highest


# In[13]:

get_highest(mydata,2)


# The errors says it's a type error.  Remember, we read in text data.  We have to convert it to numbers to compare them!  There are decimals in stock data, so we want to make them floats.

# In[14]:

def get_highest(data, column):
    highest = 0
    for row in data:
        vals = row.split(",")
        if float(vals[column]) > highest:
            highest = float(vals[column])
    return highest


# In[15]:

get_highest(mydata, 2)


# ### Homework Question 1:
# Write the function called "get_lowest", and make it similar. It should take the same arguments, the data set and the column number. Show it working with the column index for Low. 
# 
# Hint: set the initial value of your variable to float("inf"), which is infinity.
# 
# Your answer to q1:---------------------

# In[22]:

# fix this so it does as required above
def get_lowest(data, column):
    lowest = float("inf")
    for row in data:
        vals = row.split(",")
        if float(vals[column]) < lowest:
            lowest = float(vals[column])
    return lowest


# In[26]:

#show it working with the Low column number
get_lowest(mydata, 1)


# moving on...--------------------------------

# ### Homework Question 2:
# 
# Now write a function that calculates the difference between the day's open and close stock price (Close - Open), and return it. Name your function "get_difference".  It should take as argument a row of the dataset.

# Your answer to q2:--------------------------
# 

# In[27]:

def get_difference(row):
    vals = row.split(",")
    difference = float(vals[4]) - float(vals[1])
    return difference


# In[108]:

#Show it working on a row in the mydata dataset:


# In[29]:

get_difference(mydata[1])


# moving on...------------------------------

# ## Tuples: Let's Return the Date, too
# 
# We didn't talk about "tuples" in the bootcamp, but they are like short lists.  We use parentheses to indicate them: (item1, item2).  We can use a tuple to return the date too.  We index the values the same way we do with lists, 0 for the first item and 1 for the second, etc.
# 
# Please read this on tuples: https://www.tutorialspoint.com/python/python_tuples.htm .
# [Note that it was written in Python 2 -- the difference is in the print statement.  In Python 3, we use `print(thing)`, in Python 2, `print thing`.]
# 
# Then read the chapter in Trinket, to remind yourself of the dictionaries .items() and .keys() as well, which return tuples: https://books.trinket.io/pfe/10-tuples.html

# In[97]:

def get_highest_with_date(data, column):
    # take a list of rows and a column number, then return a tuple pair
    highest = (0,0)
    for row in data:
        vals = row.split(",")
        # remember these are the cols: 'Date,Open,High,Low,Close,Volume\n'
        if float(vals[column]) > highest[1]:
            # we check the value in the second element using highest[1].
            # then we assign the tuple to highest, using parens.  vals[0] is the date!
            highest = (vals[0], float(vals[column]))
    # now we return the tuple
    return highest


# In[94]:

get_highest_with_date(mydata, 1)


# In[95]:

get_highest_with_date(mydata, 3)  # using the 4th column instead...


# If we want to use the results from the function, we must save to a variable or variables:
#     

# In[98]:

date, value = get_highest_with_date(mydata, 1)


# In[102]:

print("The date of the highest value was {}".format(date))
print("The highest value was {}".format(value))


# You can also save them into a single variable, but the resulting variable will still be a tuple:
#     

# In[103]:

results = get_highest_with_date(mydata, 1)


# In[104]:

type(results)


# In[106]:

print(results[0])


# ### Homework Question 3
# 
# Rewrite your get_lowest function to return a tuple with the date of the lowest, as well as the closing value on that date.  Name your function "get_lowest_with_date".  It should take 2 arguments, the dataset and the column number for the lowest.
# 
# Your answer to q3: ------------------------------------

# In[30]:

def get_lowest_with_date(data, column):
    lowest = (0,float("inf"))
    for row in data:
        vals = row.split(",")
        # remember these are the cols: 'Date,Open,High,Low,Close,Volume\n'
        if float(vals[column]) < lowest[1]:
            # we check the value in the second element using highest[1].
            # then we assign the tuple to highest, using parens.  vals[0] is the date!
            lowest = (vals[0], float(vals[column]))
    # now we return the tuple
    return lowest


# In[33]:

get_lowest_with_date(mydata, 3)


# moving on... -----------------------------

# ## Dictionaries Again
# 
# We did dictionaries at the end of the Python Bootcamp.  Let's review a little bit.  If we wanted to store each row in a dictionary using the date as the key, we could do it like this:

# In[119]:

def make_dict(data):
    mydict = {}
    for row in data:
        vals = row.split(',')
        mydict[vals[0]] = vals[1:]
    return mydict


# In[120]:

dictdata = make_dict(mydata)


# In[121]:

dictdata.keys()


# In[122]:

dictdata.values()


# Notice there is a bad "\n" character in here. Also, notice that some of the lists don't have all the same number of elements.  Volume is missing from a bunch of dates. Let's use "strip" to clean the "\n" up and also do a bunch of list comprehensions to clean and change the data to numbers:

# In[37]:

def make_dict(data):
    mydict = {}
    for row in data:
        vals = row.split(',')
        # this is a list comprehension that applies strip to remove whitespace chars including
        # \n from each value in the vals list, then reassigns the result to vals, overwriting
        # the previous messy list.
        vals = [val.strip() for val in vals]
        # another list comprehension -- now we turn everything into a floating point number,
        # except for the first value, which is the date string and except for the empty strings.
        # There is an if-test to rule out the '' empty strings!
        floats = [float(val) for val in vals[1:] if val != '']
        # now we save the floats list to the dictionary using the date, the first item, as key
        mydict[vals[0]] = floats
    return mydict


# In[38]:

dictdata = make_dict(mydata)


# In[39]:

dictdata.values()


# Notice the results are a list of lists, but the type is a dict_values.  That means using indexing to access or slice values won't work:

# In[146]:

dictdata.values()[0]


# But we can convert to a list easily and then do it:

# In[147]:

list(dictdata.values())[0]


# How would we find which dates have closing volume and which don't? We can check the length of the lists in each key.

# In[149]:

for key, value in dictdata.items():
    if len(value) == 5:
        print("Date {} has volume of {}".format(key, value[4]))


# ### Homework 4

# Write a function called "get_volume_data" that takes the data dictionary and returns a new dictionary of just the dates and closing volume values, if it's there.  
# 
# Your answer to q4:-----------------------------

# In[35]:

def get_volume_data(dictionary):
    newdict = {}
    for key, value in dictionary.items():
        if len(value) == 5:
            newdict[key] = value[4]
    return newdict


# In[40]:

#show it running -- this should execute without an error:
volumedict = get_volume_data(dictdata)


# In[41]:

# show a row in the new dict -- this should also run without error.
list(volumedict.items())[0]


# moving on... -------------------------

# Remember that dictionaries aren't ordered. But our data is inherently ordered by date.  Luckily, there is a special type of dictionary called OrderedDict that will retain order for us.  It lives in the collections library, just like the useful Counter does.  The documentation is here: https://docs.python.org/3/library/collections.html#collections.OrderedDict

# In[153]:

from collections import OrderedDict


# In[160]:

# We create one using a sorted version of the dict we made, sorting by the first value in items, 
# which is the date:
ordereddata = OrderedDict(sorted(dictdata.items(), key=lambda x: x[0]))


# In[161]:

type(ordereddata)


# In[162]:

#Now we can verify that the keys are in order:
ordereddata.keys()


# That means that the data is too... so we can get all the values for the low and high and make charts if we want.  The basic charting tools in Python are Matplotlib, which is not very easy to use.  We will not do complex things with it.  Seaborn is a tool that improves your charting options a bit, and makes things look better.  As soon as you import it, it improves your chart style, without having to do anything!  You want to use these 3 lines all the time:

# In[44]:

import matplotlib.pyplot as plt
import seaborn
# the following line means "put my charts inside the notebook, instead of somewhere else."
get_ipython().magic('matplotlib inline')


# In[215]:

highs = [val[1][2] for val in list(ordereddata.items())]


# In[216]:

highs


# In[217]:

plt.plot(highs)


# It's obvious we would want the dates along the x-axis, to see when the peak occurred. But doing that requires a bit more work.  It's simpler for us to do it using pandas, the next topic.  The convention is to import it as "pd":

# In[43]:

import pandas as pd


# In[227]:

# Pandas has built-in tools to read files, including csv and excel.
mydf = pd.read_csv("data/goog.csv")


# In[228]:

mydf.head()  # this command shows us the result of the operation, with the top 5 rows of the table


# In[229]:

type(mydf)


# The primary data type in pandas is a DataFrame.  It has a lot of things defined on it, including plotting commands:

# In[230]:

# To make a plot from pandas, we use the dataframe object we created, then tell the plot function
# what to use as the X column and what to use as the Y column.
mydf.plot("Date", "High")


# In[231]:

mydf["Date"]


# In[232]:

# If we plot volume, we can see how little data is there with volume, all at the end:
mydf.plot("Date", "Volume")


# In[233]:

# there are some more useful functions for the new dataframe, which will help us 
# clean and check that data is valid.  .describe() does simple descriptive stats for the quantitative data.
mydf.describe()


# Now we can see the min and max, and check if we were right!

# In[244]:

get_highest(mydata, 2)


# We can also save out a csv file from pandas in a simple way.  What if we only wanted some of the columns? We can pick which ones to write out.
# 

# In[251]:

mydf.to_csv("data/saved_goog.csv")


# In[250]:

ls data


# In[252]:

mydf.to_csv("data/saved_goog_highs.csv", columns=["Date", "High"])


# In[253]:

ls data


# As is, this results in a file with the contents that start...:
# 
# ````
# ,Date,High
# 0,2010-01-04,314.44
# 1,2010-01-05,313.61
# 2,2010-01-06,312.62
# 3,2010-01-07,304.7
# 4,2010-01-08,301.32
# 5,2010-01-11,301.93
# 6,2010-01-12,298.78
# 7,2010-01-13,293.9
# 8,2010-01-14,296.8
# 9,2010-01-15,296.48
# ````
# 
# 
# If you don't want the extra index row with the rownumber and no header, you can prevent that from being saved by saying "index=None").
# 

# In[254]:

mydf.to_csv("data/saved_goog_highs.csv", columns=["Date", "High"], index=None)


# ### Homework 5
# 
# Use pandas to read in the csv file "more_data.csv" and show descriptive statistics with .describe().  Then plot the High Values by date as we did above.  Save out the file with just the High values and date, and no index column.
# 
# Your answer to q5: ------------------------

# In[45]:

mynewdf = pd.read_csv("data/more_data.csv")


# In[47]:

mynewdf.describe()


# In[48]:

mynewdf.plot("Date", "High")


# In[49]:

mynewdf.to_csv("data/new_highs.csv", columns=["Date","High"], index=None)


# Moving on.... ----------------------
# 
# ### Your reading for the week is the introductions to Pandas here:
#     
# * [Long Link Here](http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb)
# * [Another long link](http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/v0.1/cookbook/Chapter%201%20-%20Reading%20from%20a%20CSV.ipynb)
# * And feel free to watch anything you want here: http://www.dataschool.io/easier-data-analysis-with-pandas/
#         
# 

# In[ ]:



