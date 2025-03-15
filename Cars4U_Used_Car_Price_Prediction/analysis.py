import pandas as pd 
from datetime import datetime



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
    