# In this series we will review the basics of panda and play with some sort of 
# Pandas is a library that allow us to work with data that can be order or study in rows and columns
# search in google: pandas python and in pandas.pydata you can find more about it.

# In the tutorial they use pandas 0.24.1, we have 1.0.5
# We are going to use data set from kaggle, no affiliation just a cool place to get data sets
# To use kaggle we need to create an acounts, mine is sergio leiva or sergioleiva1
# We are going to use the data sets avocado prices, first.


####################################
############   Part 1   ############
####################################

# First, we download the data set and save it in a directory, that in the tutorial they call: datasets.
# Also, they use jupyter notebooks, do as you please.

import pandas as pd      # Standard import 

# Data frame --> df :  rows and columns
# series            :  rows
# pannels           :  (advanced) multiple data frame like a 3-dimensional frame

df = pd.read_csv("datasets/avocado.csv")                  # Read a csv document. In our case the avocado prices data set.

# We can print a data frame, but it shows a mayor amount of data and it would be hard to debug.

df.head()                                                 # See the first n rows, the default is 5
df.head(3)

df.tail(2)                                                # See the last n rows.