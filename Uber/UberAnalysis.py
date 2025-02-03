import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


# Allows ease and relative pull of csv file.
df = pd.read_csv(os.path.dirname(__file__) + "\\Uber.csv")

print(df.head())#View the first 5 rows to get a feel of the data

print(df.tail()) #View the last 5 rows of data as well

#PRE-PROCESS THE DATA (EDA)
"""borough - Needs evaluated. Has NULLs - why? fix?
    pickup_dt - Dtype needs chnaged from object to datetime."""
print(df.info())

print(df.describe())



#What are the different variables that influence pickups?


#Which factor affects the pickups the most? What could be plausible reasons for that?


#What are your recommendations to Uber management to capitalize on fluctuating demand?