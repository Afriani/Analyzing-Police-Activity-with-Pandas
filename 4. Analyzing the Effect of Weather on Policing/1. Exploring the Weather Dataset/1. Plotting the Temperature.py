# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import Pandas
import pandas as pd

# Import package
from urllib.request import urlretrieve

# Specify the url
url = 'https://assets.datacamp.com/production/repositories/1497/datasets/02f3fb2d4416d3f6626e1117688e0386784e8e55/weather.csv'

# Save file locally
urlretrieve(url, 'C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/weather.csv')

# Read 'weather.csv' into a DataFrame named ri
weather = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/weather.csv')

#print(weather)

# Describe the temperature columns
print(weather[['TMIN', 'TAVG', 'TMAX']].describe())

# Create a box plot of the temperature columns
weather[['TMIN', 'TAVG', 'TMAX']].plot(kind='box')

# Display the plot
plt.show()