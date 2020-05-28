# Import Pandas
import pandas as pd

# Read the DataFrame
ri = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/police.csv')

# Drop the 'county_name' and 'state' columns and defined as a new DataFrame called 'ri_col
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)