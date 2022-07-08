# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("./Document/Dataset/earthquake-database/database.csv")

#Check the data type of our date column
print(earthquakes['Date'].head())

#checking the length of each entry in the "Date" column.
date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()


#Convert our date columns to datetime (Date culumn)
#Create a new column "date_parsed" in the earthquakes dataset that has correctly parsed dates in it.
earthquakes['date_parsed']= pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")
earthquakes['date_parsed'].head()

#Create a Pandas Series day_of_month_earthquakes containing the day of the month from the "date_parsed" column.
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day
day_of_month_earthquakes.head()


# Plot the day of the month to check the date parsing
sns.distplot(day_of_month_earthquakes, kde=False, bins=31)