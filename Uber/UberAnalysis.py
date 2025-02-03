import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

"""
STEPPED PROCESS WITH COMMENTS OF LOGIC INCLUDED
"""

# Allows ease and relative pull of csv file.
df = pd.read_csv(os.path.dirname(__file__) + "\\Uber.csv")

print(df.head())#View the first 5 rows to get a feel of the data

print(df.tail()) #View the last 5 rows of data as well

#PRE-PROCESS THE DATA (EDA)
"""borough - Needs evaluated. Has NULLs - Determine proper handling
    pickup_dt - Dtype needs chnaged from object to datetime.
    borough and hday should be string categories."""
print(df.info())


"""The max in pickups and sd (snow depth) is significantly higher than even the 3rd (75%) Quartile. 
Need to evaluate why - is there bad data? A Bad Entry?

"""

print(df.describe().T)
#Check the summary of non-numeric numbers
"""Here we see that Bronx and N for borough and hday respectively are the top occurences in the data.
for hday, that makes sense as the frequency is almost 28k out of the just over 29k.
"""
print(df.describe(exclude = 'number').T)
print('-----------------------------------------')
"""This shows that all categories in borough occur equally. Proving there is no true Mode"""
#Check that 'Bronx' is really the MODE of the borough category.
print(df['borough'].value_counts())

#What are the different variables that influence pickups?


#Which factor affects the pickups the most? What could be plausible reasons for that?


#What are your recommendations to Uber management to capitalize on fluctuating demand?