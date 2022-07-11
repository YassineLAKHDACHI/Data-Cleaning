# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

with open("./Documennts/Dataset/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv" ,'rb') as rawdata:
   result = chardet.detect(rawdata.read(10000))
print(result)

# Read im the file to a DataFrame police_killings.
police_killings= pd.read_csv("./Documennts/Dataset/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='windows-1252')
police_killings.head()

# Save a version of the police killings dataset to CSV with UTF-8 encoding
police_killings.to_csv("/kaggle/working/my_file.csv")

