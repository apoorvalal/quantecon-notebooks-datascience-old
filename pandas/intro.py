# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.3.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] Collapsed="false"
# # Introduction
#
# **Prerequisites**
#
# - [Python Fundamentals](../python_fundamentals/index.html)  
#
#
# **Outcomes**
#
# - Understand the core pandas objects (`Series` and `DataFrame`)  
# - Index into particular elements of a Series and DataFrame  
# - Understand what `.dtype`/`.dtypes` do  
# - Make basic visualizations  
#
#
# **Data**
#
# - US regional unemployment data from Bureau of Labor Statistics  

# %% [markdown] Collapsed="false"
# ## Outline
#
# - [Introduction](#Introduction)  
#   - [pandas](#pandas)  
#   - [Series](#Series)  
#   - [DataFrame](#DataFrame)  
#   - [Data Types](#Data-Types)  
#   - [Changing DataFrames](#Changing-DataFrames)  
#   - [Exercises](#Exercises)  

# %% Collapsed="false" hide-output=false
# Uncomment following line to install on colab
#! pip install qeds

# %% [markdown] Collapsed="false"
# ## pandas
#
# This lecture begins the material on `pandas`.
#
# To start, we will import the pandas package and give it the alias
# `pd`, which is conventional practice.

# %% Collapsed="false" hide-output=false
import pandas as pd

# Don't worry about this line for now!
%matplotlib inline
# activate plot theme
import qeds
qeds.themes.mpl_style();

# %% [markdown] Collapsed="false"
# Sometimes, knowing which pandas version we are
# using is helpful.
#
# We can check this by running the code below.

# %% Collapsed="false" hide-output=false
pd.__version__

# %% [markdown] Collapsed="false"
# ## Series
#
# The first main pandas type we will introduce is called Series.
#
# A Series is a single column of data, with row labels for each
# observation.
#
# pandas refers to the row labels as the *index* of the Series.
#
# ![https://storage.googleapis.com/ds4e/_static/intro_files/PandasSeries.png](https://storage.googleapis.com/ds4e/_static/intro_files/PandasSeries.png)  
# Below, we create a Series which contains the US unemployment rate every
# other year starting in 1995.

# %% Collapsed="false" hide-output=false
values = [5.6, 5.3, 4.3, 4.2, 5.8, 5.3, 4.6, 7.8, 9.1, 8., 5.7]
years = list(range(1995, 2017, 2))

unemp = pd.Series(data=values, index=years, name="Unemployment")

# %% Collapsed="false" hide-output=false
unemp

# %% [markdown] Collapsed="false"
# We can look at the index and values in our Series.

# %% Collapsed="false" hide-output=false
unemp.index

# %% Collapsed="false" hide-output=false
unemp.values

# %% [markdown] Collapsed="false"
# ### What Can We Do with a Series object?

# %% [markdown] Collapsed="false"
# #### `.head` and `.tail`
#
# Often, our data will have many rows, and we won’t want to display it all
# at once.
#
# The methods `.head` and `.tail` show rows at the beginning and end
# of our Series, respectively.

# %% Collapsed="false" hide-output=false
unemp.head()

# %% Collapsed="false" hide-output=false
unemp.tail()

# %% [markdown] Collapsed="false"
# #### Basic Plotting
#
# We can also plot data using the `.plot` method.

# %% Collapsed="false" hide-output=false
unemp.plot()

# %% [markdown] Collapsed="false"
# >**Note**
# >
# >This is why we needed the `%matplotlib inline` — it tells the notebook
# to display figures inside the notebook itself. Also, pandas has much greater visualization functionality than this, but we will study that later on.

# %% [markdown] Collapsed="false"
# #### Unique Values
#
# Though it doesn’t make sense in this data set, we may want to find the
# unique values in a Series – which can be done with the `.unique` method.

# %% Collapsed="false" hide-output=false
unemp.unique()

# %% [markdown] Collapsed="false"
# #### Indexing
#
# Sometimes, we will want to select particular elements from a Series.
#
# We can do this using `.loc[index_items]`; where `index_items` is
# an item from the index, or a list of items in the index.
#
# We will see this more in-depth in a coming lecture, but for now, we
# demonstrate how to select one or multiple elements of the Series.

# %% Collapsed="false" hide-output=false
unemp.loc[1995]

# %% Collapsed="false" hide-output=false
unemp.loc[[1995, 2005, 2015]]

# %% [markdown] Collapsed="false"
#
# <a id='exercise-0'></a>
# > See exercise 1 in the [*exercise list*](#exerciselist-0)

# %% [markdown] Collapsed="false"
# ## DataFrame
#
# A DataFrame is how pandas stores one or more columns of data.
#
# We can think a DataFrames a multiple Series stacked side by side as
# columns.
#
# This is similar to a sheet in an Excel workbook or a table in a SQL
# database.
#
# In addition to row labels (an index), DataFrames also have column labels.
#
# We refer to these column labels as the columns or column names.
#
# ![https://storage.googleapis.com/ds4e/_static/intro_files/PandasDataFrame.png](https://storage.googleapis.com/ds4e/_static/intro_files/PandasDataFrame.png)  
# Below, we create a DataFrame that contains the unemployment rate every
# other year by region of the US starting in 1995.

# %% Collapsed="false" hide-output=false
data = {
    "NorthEast": [5.9,  5.6,  4.4,  3.8,  5.8,  4.9,  4.3,  7.1,  8.3,  7.9,  5.7],
    "MidWest": [4.5,  4.3,  3.6,  4. ,  5.7,  5.7,  4.9,  8.1,  8.7,  7.4,  5.1],
    "South": [5.3,  5.2,  4.2,  4. ,  5.7,  5.2,  4.3,  7.6,  9.1,  7.4,  5.5],
    "West": [6.6, 6., 5.2, 4.6, 6.5, 5.5, 4.5, 8.6, 10.7, 8.5, 6.1],
    "National": [5.6, 5.3, 4.3, 4.2, 5.8, 5.3, 4.6, 7.8, 9.1, 8., 5.7]
}

unemp_region = pd.DataFrame(data, index=years)
unemp_region

# %% [markdown] Collapsed="false"
# We can retrieve the index and the DataFrame values as we
# did with a Series.

# %% Collapsed="false" hide-output=false
unemp_region.index

# %% Collapsed="false" hide-output=false
unemp_region.values

# %% [markdown] Collapsed="false"
# ### What Can We Do with a DataFrame?
#
# Pretty much everything we can do with a Series.

# %% [markdown] Collapsed="false"
# #### `.head` and `.tail`
#
# As with Series, we can use `.head` and `.tail` to show only the
# first or last `n` rows.

# %% Collapsed="false" hide-output=false
unemp_region.head()

# %% Collapsed="false" hide-output=false
unemp_region.tail(3)

# %% [markdown] Collapsed="false"
# #### Plotting
#
# We can generate plots with the `.plot` method.
#
# Notice we now have a separate line for each column of data.

# %% Collapsed="false" hide-output=false
unemp_region.plot()

# %% [markdown] Collapsed="false"
# #### Indexing
#
# We can also do indexing using `.loc`.
#
# This is slightly more advanced than before because we can choose
# subsets of both row and columns.

# %% Collapsed="false" hide-output=false
unemp_region.loc[1995, "NorthEast"]

# %% Collapsed="false" hide-output=false
unemp_region.loc[[1995, 2005], "South"]

# %% Collapsed="false" hide-output=false
unemp_region.loc[1995, ["NorthEast", "National"]]

# %% Collapsed="false" hide-output=false
unemp_region.loc[:, "NorthEast"]

# %% Collapsed="false" hide-output=false
# `[string]` with no `.loc` extracts a whole column
unemp_region["MidWest"]

# %% [markdown] Collapsed="false"
# ### Computations with Columns
#
# pandas can do various computations and mathematical operations on
# columns.
#
# Let’s take a look at a few of them.

# %% Collapsed="false" hide-output=false
# Divide by 100 to move from percent units to a rate
unemp_region["West"] / 100

# %% Collapsed="false" hide-output=false
# Find maximum
unemp_region["West"].max()

# %% Collapsed="false" hide-output=false
# Find the difference between two columns
# Notice that pandas applies `-` to _all rows_ at once
# We'll see more of this throughout these materials
unemp_region["West"] - unemp_region["MidWest"]

# %% Collapsed="false" hide-output=false
# Find correlation between two columns
unemp_region.West.corr(unemp_region["MidWest"])

# %% Collapsed="false" hide-output=false
# find correlation between all column pairs
unemp_region.corr()

# %% [markdown] Collapsed="false"
#
# <a id='exercise-1'></a>
# > See exercise 2 in the [*exercise list*](#exerciselist-0)

# %% [markdown] Collapsed="false"
# ## Data Types
#
# We asked you to run the commands `unemp.dtype` and
# `unemp_region.dtypes` and think about the outputs.
#
# You might have guessed that they return the type of the values inside
# each column.
#
# Occasionally, you might need to investigate what types you have in your
# DataFrame when an operation isn’t behaving as expected.

# %% Collapsed="false" hide-output=false
unemp.dtype

# %% Collapsed="false" hide-output=false
unemp_region.dtypes

# %% [markdown] Collapsed="false"
# DataFrames will only distinguish between a few types.
#
# - Booleans (`bool`)  
# - Floating point numbers (`float64`)  
# - Integers (`int64`)  
# - Dates (`datetime`) — we will learn this soon  
# - Categorical data (`categorical`)  
# - Everything else, including strings (`object`)  
#
#
# In the future, we will often refer to the type of data stored in a
# column as its `dtype`.
#
# Let’s look at an example for when having an incorrect `dtype` can
# cause problems.
#
# Suppose that when we imported the data the `South` column was
# interpreted as a string.

# %% Collapsed="false" hide-output=false
str_unemp = unemp_region.copy()
str_unemp["South"] = str_unemp["South"].astype(str)
str_unemp.dtypes

# %% [markdown] Collapsed="false"
# Everything *looks* ok…

# %% Collapsed="false" hide-output=false
str_unemp.head()

# %% [markdown] Collapsed="false"
# But if we try to do something like compute the sum of all the columns,
# we get unexpected results…

# %% Collapsed="false" hide-output=false
str_unemp.sum()

# %% [markdown] Collapsed="false"
# This happened because `.sum` effectively calls `+` on all rows in
# each column.
#
# Recall that when we apply `+` to two strings, the result is the two
# strings concatenated.
#
# So, in this case, we saw that the entries in all rows of the South
# column were stitched together into one long string.

# %% [markdown] Collapsed="false"
# ## Changing DataFrames
#
# We can change the data inside of a DataFrame in various ways:
#
# - Adding new columns  
# - Changing index labels or column names  
# - Altering existing data (e.g. doing some arithmetic or making a column
#   of strings lowercase)  
#
#
# Some of these “mutations” will be topics of future lectures, so we will
# only briefly discuss a few of the things we can do below.

# %% [markdown] Collapsed="false"
# ### Creating New Columns
#
# We can create new data by assigning values to a column similar to how
# we assign values to a variable.
#
# In pandas, we create a new column of a DataFrame by writing:

# %% [markdown] Collapsed="false" hide-output=false
# ```python
# df["New Column Name"] = new_values
# ```
#

# %% [markdown] Collapsed="false"
# Below, we create an unweighted mean of the unemployment rate across the
# four regions of the US — notice that this differs from the national
# unemployment rate.

# %% Collapsed="false" hide-output=false
unemp_region["UnweightedMean"] = (unemp_region["NorthEast"] +
                                  unemp_region["MidWest"] +
                                  unemp_region["South"] +
                                  unemp_region["West"])/4

# %% Collapsed="false" hide-output=false
unemp_region.head()

# %% [markdown] Collapsed="false"
# ### Changing Values
#
# Changing the values inside of a DataFrame should be done sparingly.
#
# However, it can be done by assigning a value to a location in the
# DataFrame.
#
# `df.loc[index, column] = value`

# %% Collapsed="false" hide-output=false
unemp_region.loc[1995, "UnweightedMean"] = 0.0

# %% Collapsed="false" hide-output=false
unemp_region.head()

# %% [markdown] Collapsed="false"
# ### Renaming Columns
#
# We can also rename the columns of a DataFrame, which is helpful because the names that sometimes come with datasets are
# unbearable…
#
# For example, the original name for the North East unemployment rate
# given by the Bureau of Labor Statistics was `LASRD910000000000003`…
#
# They have their reasons for using these names, but it can make our job
# difficult since we often need to type it repeatedly.
#
# We can rename columns by passing a dictionary to the `rename` method.
#
# This dictionary contains the old names as the keys and new names as the
# values.
#
# See the example below.

# %% Collapsed="false" hide-output=false
names = {"NorthEast": "NE",
         "MidWest": "MW",
         "South": "S",
         "West": "W"}
unemp_region.rename(columns=names)

# %% Collapsed="false" hide-output=false
unemp_region.head()

# %% [markdown] Collapsed="false"
# We renamed our columns… Why does the DataFrame still show the old
# column names?
#
# Many pandas operations create a copy of your data by
# default to protect your data and prevent you from overwriting
# information you meant to keep.
#
# We can make these operations permanent by either:
#
# 1. Assigning the output back to the variable name
#   `df = df.rename(columns=rename_dict)`  
# 1. Looking into whether the method has an `inplace` option. For
#   example, `df.rename(columns=rename_dict, inplace=True)`  
#
#
# Setting `inplace=True` will sometimes make your code faster
# (e.g. if you have a very large DataFrame and you don’t want to copy all
# the data), but that doesn’t always happen.
#
# We recommend using the first option until you get comfortable with
# pandas because operations that don’t alter your data are (usually)
# safer.

# %% Collapsed="false" hide-output=false
names = {"NorthEast": "NE",
         "MidWest": "MW",
         "South": "S",
         "West": "W"}

unemp_shortname = unemp_region.rename(columns=names)
unemp_shortname.head()

# %% [markdown] Collapsed="false"
# ## Exercises
#
#
# <a id='exerciselist-0'></a>
# **Exercise 1**
#
# For each of the following exercises, we recommend reading the documentation
# for help.
#
# - Display only the first 2 elements of the Series using the `.head` method.  
# - Using the `plot` method, make a bar plot.  
# - Use `.loc` to select the lowest/highest unemployment rate shown in the Series.  
# - Run the code `unemp.dtype` below. What does it give you? Where do you think it comes from?  
#
#
# ([*back to text*](#exercise-0))
#
# **Exercise 2**
#
# For each of the following, we recommend reading the documentation for help.
#
# - Use introspection (or google-fu) to find a way to obtain a list with
#   all of the column names in `unemp_region`.  
# - Using the `plot` method, make a bar plot. What does it look like
#   now?  
# - Use `.loc` to select the the unemployment data for the
#   `NorthEast` and `West` for the years 1995, 2005, 2011, and 2015.  
# - Run the code `unemp_region.dtypes` below. What does it give you?
#   How does this compare with `unemp.dtype`?  
#
#
# ([*back to text*](#exercise-1))
