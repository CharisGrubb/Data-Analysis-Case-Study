import pandas as pd 
from datetime import datetime

# Import libraries to build linear model for statistical analysis and prediction
from sklearn.linear_model import LinearRegression, Ridge, Lasso # Importing Linear Regression, and Regularization methods
from sklearn.tree import DecisionTreeRegressor # Importing Decision Tree Regressor
from sklearn.ensemble import RandomForestRegressor # Importing Random Forest Regressor
from sklearn.model_selection import train_test_split # To split the data into training and test set

# Metrics to evaluate the model
from sklearn import metrics # To calculate the accuracy metrics

# For tuning the model
from sklearn.model_selection import GridSearchCV # For tuning parameters of the model



def analyze():
    with open('Cars4U_Used_Car_Price_Prediction\\analysis_output.txt','w') as file:
        start_time = datetime.now()
        file.write(f"START ANALYSIS: {start_time}")

        data = pd.read_csv("Cars4U_Used_Car_Price_Prediction\\used_cars_data.csv")
        data_copy = data.copy()
     
        #Log Dataset  Information
        file.write("\nDataset shape: " + str(data_copy.shape))
        file.write("\n\nData Stats: \n" + str(data_copy.describe()))

        #Check for NULL values
        total_rows = data_copy.shape[0]
        for col in data_copy.columns:
            col_non_null = data_copy[col].count()
            if col_non_null< total_rows:
                file.write(f"\n {col} is missing {total_rows-col_non_null} values.")


        end_time = datetime.now()
        file.write(f"\n\nEND ANALYSIS: {end_time}" )
        file.write("\nTIME TOOK: " + str((end_time - start_time).seconds) + " seconds.")


# Making unit same across whole column
def mileage_convert(x): # Function to convert km/kg to km per liter
    if type(x) == str: # if the data type is string
        if x.split()[-1] == 'km/kg': # If the unit is km/kg towards the end of the string, split the string into 'at km/kg' where the number is separated from the text
            return float(x.split()[0])*1.40 # Formula for converting km/kg to kmpl for the number part of the text that is already split, by converting text to float type
        elif x.split()[-1] == 'kmpl': # If the text is 'kmpl' instead of 'km/kg', then split at 'kmpl'
            return float(x.split()[0]) # Then convert that to float type for the data which is separated from 'kmpl'
    else:
        return x # If there is no 'kmpl' or 'km/kg', then we are good, no action needs to be taken.

def price_convert(x): # Function to extract the numerical price data from the column which has the value of "amount Cr." OR "amount Lakh"
    if type(x) == str: # If the data type is string (text data a.k.a. object)
        if x.split()[-1] == 'Cr': # Split the value in 'Cr', the last part of the values
            return float(x.split()[0])*100 # Formula for converting Crores to Lakhs: divide the data value in index[0] by 100

        elif x.split()[-1] == 'Lakh': # If the string contains "Lakh", split the data at the word "Lakh".
            return float(x.split()[0]) # Then keep the number part from the splitted data.
    else:
        return x  # If neither "Lakh" nor "Cr." is present, keep the data as it is.

