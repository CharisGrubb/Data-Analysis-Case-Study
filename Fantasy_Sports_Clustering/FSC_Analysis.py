
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
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Goals_Scored,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_goalsscored.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Assists,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_assists.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Goals_Conceded,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_goalsconceded.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Clean_Sheets,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_cleansheets.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Minutes,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_mins.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Total_Points,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_totalpnts.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Creativity,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_creativity.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Influence,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_influence.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Threat,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_threat.png")
        plotter.Plotter_Helper.box_hist_plot(x= data_copy.Bonus,save_path="Fantasy_Sports_Clustering\\Plots\\histoboxplot_bonus.png")
        
        
        
        
        file.close()