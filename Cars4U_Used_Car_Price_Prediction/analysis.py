import pandas as pd 
from datetime import datetime



def analysis():
    with open('Cars4U_Used_Car_Price_Prediction\\analysis_output.txt','w') as file:
        start_time = datetime.now()
        file.write(f"START ANALYSIS: {start_time}")

        data = pd.read_csv("Cars4U_Used_Car_Price_Prediction\\used_cars_data.csv")
        data_copy = data.copy()

        file.write("\nDataset shape: " + str(data_copy.shape()))
        file.write("\nData Stats: \n")
        file.write(data_copy.describe())