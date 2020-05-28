# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import Pandas
import pandas as pd

# Read 'weather.csv' into a DataFrame named ri
weather = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/weather.csv')

# Create a 'TDIFF' column that represents temperature difference
weather['TDIFF']= weather.TMAX - weather.TMIN

# Describe the 'TDIFF' column
print(weather.TDIFF.describe())

# Create a histogram with 20 bins to visualize 'TDIFF'
weather.TDIFF.plot(kind='hist', bins=20)

# Display the plot
plt.show()