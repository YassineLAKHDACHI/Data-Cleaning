# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("C:/Users/Yqssine/Documents/Technocholabes_Internship/Dataset/Building_Permits.csv")

#print the first five rows of the sf_permits DataFrame
sf_permits.head()

#percentage of the values in the dataset are missing
missing_values_count = sf_permits.isnull().sum()
total_cells = np.product(sf_permits.shape)
total_missing = missing_values_count.sum()

percent_missing = (total_missing/total_cells) * 100
print(percent_missing)


#Drop missing values: rows || this will remove all the rows in the dataset
sf_permits.dropna()

#Create a new DataFrame called "sf_permits_with_na_dropped"
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

#The number of columns removed from the original sf_permits DataFrame
original_dataset = sf_permits.shape[1]
na_dropped = sf_permits_with_na_dropped.shape[1]
dropped_columns = original_dataset - na_dropped

#replacing all the NaN's in the sf_permits data with the one that comes directly after it
#then replacing any remaining NaN's with 0.
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)
