# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import Pandas
import pandas as pd

# Read the DataFrame
ri = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/police.csv')

# Drop the 'county_name' and 'state' columns and defined as a new DataFrame called 'ri_col
ri.drop(['county_name', 'state'], axis='columns', inplace=True)

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min' : 8, '16-30 Min' : 23, '30+ Min' : 45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
#print(ri.groupby('violation_raw').stop_minutes.mean())

print(ri.head())

# Save the resulting Series as 'stop_length'
#stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
#stop_length.sort_values().plot(kind='barh')

# Display the plot
#plt.show()