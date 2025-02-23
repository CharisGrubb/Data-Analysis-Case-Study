
from utility import plotter, unsup_cluster
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def analyze():
    with open('Fantasy_Sports_Clustering\\analysis_output.txt','w') as file:
        data = pd.read_csv("Fantasy_Sports_Clustering\\fpl_data.csv")
        data_copy = data.copy() #Copy in order to maintain original data for reference

        #Log the dataset shape
        rows,cols = data.shape
        file.write(f"Rows/Columns: {rows}/{cols} \n")


        dup_sum = data_copy.duplicated().sum() 
        file.write(f"Duplicate summary: {dup_sum}\n")

        data_nulls = data_copy.isnull().sum()

        file.write(f"Number of NULLs per Column:\n {data_nulls} \n")

        for i in data_nulls:
            if i>0:
                print("Add logic to fix null data-", data_nulls.index[i])
                file.write("Fixing NULL data at " + data_nulls.index[i])

        
        #Univariate Analysis
        for col in data_copy.columns:
           
            if data_copy[col].dtype in ['int64','float64']:
                plotter.Plotter_Helper.box_hist_plot(x= data_copy[col],save_path=f"Fantasy_Sports_Clustering\\Plots\\histoboxplot_{col}.png")
            elif data_copy[col].dtype in ['str', 'object']:
                plotter.Plotter_Helper.barplot(data_copy, col, save_path = f"Fantasy_Sports_Clustering\\Plots\\barplot_{col}.png")
        
        
        
        
        file.close()