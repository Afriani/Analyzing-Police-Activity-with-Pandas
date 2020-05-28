# Import package
from urllib.request import urlretrieve

# Import the pandas library as pd
import pandas as pd

# Specify the url
url = 'https://assets.datacamp.com/production/repositories/1497/datasets/62bd9feef451860db02d26553613a299721882e8/police.csv'

# Save file locally
urlretrieve(url, 'C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/police.csv')

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Police Activity with Pandas/DATA/police.csv')

# Examine the head of the DataFrame
print(ri.head())
#print(ri)

# Count the number of missing values in each column
print(ri.isnull().sum())