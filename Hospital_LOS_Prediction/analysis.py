from utility.plotter import Plotter_Helper
import pandas as pd

def analyze():
   with open('Hospital_LOS_Prediction\\analysis_output.txt','w') as file:
      data = pd.read_csv("Hospital_LOS_Prediction\\healthcare_data.csv")
      data_copy = data.copy() #Copy in order to maintain original data for reference

      file.write("Data shape: " + str(data_copy.shape))
        

         #unique identifier for patient is not needed for analysis. 
         #also dropping to help ensure patient privacy for final analysis
      data_copy = data_copy.drop(columns=['patientid'])

      for col in data_copy.columns:
         if data_copy[col].dtype in ['object','str']:
            file.write(str(data_copy[col].value_counts(1)))
            file.write("\n\n"+("-" * 50)+"\n\n")

         
      #Univariate Analysis
      for col in data_copy.columns:
         if data_copy[col].dtype in ['int64','float64']:
            Plotter_Helper.box_hist_plot(data_copy[col],f"Hospital_LOS_Prediction\\Plots\\histBox_{col}.png")
         elif data_copy[col].dtype in ['object']:
            Plotter_Helper.barplot(data_copy, col, f"Hospital_LOS_Prediction\\Plots\\bar_{col}.png")