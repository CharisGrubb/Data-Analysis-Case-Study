import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

"""
STEPPED PROCESS (WALK THROUGH) WITH COMMENTS OF LOGIC INCLUDED
"""

# Allows ease and relative pull of csv file.
df = pd.read_csv(os.path.dirname(__file__) + "\\Uber.csv")

print(df.head())#View the first 5 rows to get a feel of the data

print(df.tail()) #View the last 5 rows of data as well

#PRE-PROCESS THE DATA (EDA)
"""borough - Needs evaluated. Has NULLs - Determine proper handling
    pickup_dt - Dtype needs chnaged from object to datetime.
    borough and hday are categorical"""
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
print(df.borough.value_counts(normalize = True, dropna = False))

#Fix data types
df.pickup_dt = pd.to_datetime(df.pickup_dt)

# Replacing NaN with Unknown
df['borough'] = df['borough'].fillna('Unknown') 

"""BOX PLOTS and HISTOGRAM"""
f, (ax_box, ax_hist) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid
        sharex=True,  # The X-axis will be shared among all the subplots
        gridspec_kw={"height_ratios": (.25, .75)},
        figsize=(15,10)
    )
sns.boxplot(x=df.pickups, ax=ax_box, showmeans=True, color='red')
sns.histplot(x=df.pickups, kde=False, ax=ax_hist, bins="auto")
ax_hist.axvline(df.pickups.mean(), color='g', linestyle='--')      # Add mean to the histogram
ax_hist.axvline(df.pickups.median(), color='black', linestyle='-') # Add median to the histogram

"""Distribution of hourly pickups is highly right-skewed """
plt.savefig("Uber\\Plots\\pickups_box_hist.png")

f, (ax_box, ax_hist) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid
        sharex=True,  # The X-axis will be shared among all the subplots
        gridspec_kw={"height_ratios": (.25, .75)},
        figsize=(15,10)
    )

sns.boxplot(x=df.vsb, ax=ax_box, showmeans=True, color='red')
sns.histplot(x=df.vsb, kde=False, ax=ax_hist, bins="auto")
ax_hist.axvline(df.vsb.mean(), color='g', linestyle='--')      # Add mean to the histogram
ax_hist.axvline(df.vsb.median(), color='black', linestyle='-') # Add median to the histogram

"""Distribution of vsb (Visibility) is left-skewed """
plt.savefig("Uber\\Plots\\vsb_box_hist.png")

f, (ax_box, ax_hist) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid
        sharex=True,  # The X-axis will be shared among all the subplots
        gridspec_kw={"height_ratios": (.25, .75)},
        figsize=(15,10)
    )

sns.boxplot(x=df.sd, ax=ax_box, showmeans=True, color='red')
sns.histplot(x=df.sd, kde=False, ax=ax_hist, bins="auto")
ax_hist.axvline(df.sd.mean(), color='g', linestyle='--')      # Add mean to the histogram
ax_hist.axvline(df.sd.median(), color='black', linestyle='-') # Add median to the histogram

"""Distribution of sd (Snow Depth) """
plt.savefig("Uber\Plots\\sd_box_hist.png")

####MULTIVARIATE#############
num_var = ['pickups', 'spd', 'vsb', 'temp', 'dewp', 'slp', 'pcp01', 'pcp06', 'pcp24', 'sd']
corr = df[num_var].corr()

# Plot the heatmap
plt.figure(figsize = (14, 10))
sns.heatmap(corr, annot = True, cmap = 'coolwarm',            
        fmt = ".1f",            
        xticklabels = corr.columns,            
        yticklabels = corr.columns)
"""Dew POint (an indication of humidity) appears highly coorelated with temperature.
Visibility is negatively coorelated with precipitation - meaning, as precipitation increases, visibility goes down
Snow depth is negatively coorelated with temperature, as expected.
NOTE: Correlation does not imply causation."""
plt.savefig("Uber\\Plots\\heatmap.png")


#### # of PICKUPS GROUPED BY MONTH NAME
df['start_month'] = df.pickup_dt.dt.month_name()
cats = df.start_month.unique().tolist() #Get a list of all month start dates
df.start_month = pd.Categorical(df.start_month, ordered=True, categories = cats)#Order data
plt.figure(figsize=(20,7))
sns.lineplot(x = 'start_month', y='pickups', data=df, errorbar=('ci', 0), color="PURPLE", estimator="sum")
plt.ylabel("Total Pickups")
plt.xlabel("Month")
plt.savefig("Uber\\Plots\\PickupsByMonthName.png")


#### AVERAGE OF PICKUPS GROUPED BY WEEK DAY NAME
df['week_day'] = df.pickup_dt.dt.day_name()
cats = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
df.week_day = pd.Categorical(df.week_day, ordered = True, categories = cats)
plt.figure(figsize = (20, 7))
sns.lineplot(x = "week_day", y = "pickups", errorbar=('ci', 0), data = df, color = "RED")
plt.ylabel('AVG(Mean) pickups')
plt.xlabel('DAY OF WEEK')
"""SATURDAY has the most AVG pickups, with MONDAY being the least"""
plt.savefig("Uber\\Plots\\AVG_pickups_by_weekday.png")



