# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:20:43 2020

@author: Tapan
"""

#impoting library
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# loading iris dataset
dataset = pd.read_csv('E:/python/datascience/EDA/iris.csv')

#(Q) how amny datapoint and features
print(dataset.shape)
#(Q) what are the column name in our dataset
print(dataset.columns)
#(Q) how many data point are available for each species
dataset['species'].value_counts()
# iris dataset is balanced dataset as each no for datapoints are samre for each species.

# 2D scatter plot
#Alway understand the axis: label and scale
sns.set_style('whitegrid')
dataset.plot(kind='scatter',x ='sepal_length',y='sepal_width')
plt.show()
#it does not make any sence out her .what if we make color code for each type of flower
sns.FacetGrid(dataset,hue='species',size=4).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()
# Notice that blue point can be easily seprated from red and green point by drawing a line
# but red and green pionts can not be  easily seprated
#we can draw multiple 2D plot for each combination of feature
# how many such combination exist (4C2=6)
# Observations
# Using sepal length and sepal width We can easily seprate setosa by drawing a line
# but is hard to seprate versicolor and virginica because most points overlap each other.

# pair plot

sns.pairplot(dataset,hue='species',size=4)
plt.show()

#Observations:
# patel lenght and patel width are most useful feature to identify various flower type.
# while setosa can be easily identified (linear seperable) while versicolor and virginica 
# have some overlap(almost linearly seperable)
# we can find line and if else conditon to simply bulid a model to identify flowers.

#limitation of pair plot
# It is usefull where number of featurs are less(up to 6) .
# If the featurs are n dimensinal (100) it is not possiable to understand the data.


# Histrogram and PDF (probablity density function)
# 1 D scatter ploting just using one features(patel length)

iris_setosa = dataset.loc[dataset['species']=='setosa']
iris_virginica = dataset.loc[dataset['species']=='virginica']
iris_versicolor= dataset.loc[dataset['species']=='versicolor']

plt.plot(iris_setosa['petal_length'],np.zeros_like(iris_setosa['petal_length']),'o')
plt.plot(iris_virginica['petal_length'],np.zeros_like(iris_virginica['petal_length']),'o')
plt.plot(iris_versicolor['petal_length'],np.zeros_like(iris_versicolor['petal_length']),'o')
plt.show()
# =============================================================================
# disadvantage of 1D sactter plot: very hard to make sence beacause points are overlaping a lot. 
# Better way to visualizing 1 D scatter plot is histogram plot
# =============================================================================

sns.FacetGrid(dataset,hue='species', size=6).map(sns.distplot,'petal_length').add_legend()
sns.FacetGrid(dataset,hue='species', size=6).map(sns.distplot,'petal_width').add_legend()
sns.FacetGrid(dataset,hue='species', size=6).map(sns.distplot,'sepal_length').add_legend()
sns.FacetGrid(dataset,hue='species', size=6).map(sns.distplot,'petal_width').add_legend()
plt.show()

# =============================================================================
# Need for comulativev distribution function(CDF) 
# WE can see how percentage of flower have petyal length less than 1.6
# how to contruct CDF
# How to read CDF
# Plot CDF of Petal Length
# =============================================================================

counts,bin_edges =np.histogram(iris_setosa['petal_length'],bins=10,density=True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)

# Compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)
plt.show()









