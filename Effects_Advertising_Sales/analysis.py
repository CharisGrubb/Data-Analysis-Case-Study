import pandas as pd

def analyze():
     with open('Effects_Advertising_Sales\\analysis_output.txt','w') as file:
        data = pd.read_csv("Effects_Advertising_Sales\\Advertising.csv")
        data_copy = data.copy() #Copy in order to maintain original data for reference

        file.write("Data shape: " + str(data_copy.shape))