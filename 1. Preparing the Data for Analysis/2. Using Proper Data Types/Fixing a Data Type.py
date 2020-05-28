# Import Pandas
import pandas as pd

# Read the DataFrame
ri = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/police.csv')

# Drop the 'county_name' and 'state' columns and defined as a new DataFrame called 'ri_col
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Check the data type of 'is_arrested'
print(ri.is_arrested.dtype)

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' (again)
print(ri.is_arrested.dtype)