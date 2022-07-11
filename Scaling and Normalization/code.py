# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("./Document/Dataset/kickstarter-projects/ks-projects-201801.csv")

#SCALING

# select the usd_goal_real column
original_goal_data = pd.DataFrame(kickstarters_2017.goal)

#Use original_goal_data to create a new DataFrame scaled_goal_data with values scaled between 0 and 1.
scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])
print('Original data\nPreview:\n', original_goal_data.head())
print('Minimum value:', float(original_goal_data.min()),
      '\nMaximum value:', float(original_goal_data.max()))
print('_'*30)
print('\nScaled data\nPreview:\n', scaled_goal_data.head())
print('Minimum value:', float(scaled_goal_data.min()),
      '\nMaximum value:', float(scaled_goal_data.max()))

# NORMALIZATION  

# get the index of all positive pledges (Box-Cox only takes positive values)
index_of_positive_pledges = kickstarters_2017.pledged > 0

# get only positive pledges (using their indexes)
positive_pledges = kickstarters_2017.pledged.loc[index_of_positive_pledges]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='pledged', index=positive_pledges.index)

print('Original data\nPreview:\n', positive_pledges.head())
print('Minimum value:', float(positive_pledges.min()),
      '\nMaximum value:', float(positive_pledges.max()))
print('_'*30)

print('\nNormalized data\nPreview:\n', normalized_pledges.head())
print('Minimum value:', float(normalized_pledges.min()),
      '\nMaximum value:', float(normalized_pledges.max()))



