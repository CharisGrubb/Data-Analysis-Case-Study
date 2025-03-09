from datetime import datetime
from utility.plotter import Plotter_Helper
import pandas as pd


def analyze():
    with open('BigMart_Sales\\analysis_output.txt','w') as file:
        start_time = datetime.now()
        file.write(f"START ANALYSIS: {start_time}")

        train_df = pd.read_csv("BigMart_Sales\\Train-1.csv")
        test_df = pd.read_csv("BigMart_Sales\\Test-1.csv")

    
        file.write("\n\nTRAIN Dataset SHAPE: " + str(train_df.shape))
        file.write("\nTEST Dataset SHAPE: " + str(test_df.shape))

        #Remove Unique Identifiers as they will only skew the data. 
        train_df = train_df.drop(['Item_Identifier', 'Outlet_Identifier'], axis = 1)
        test_df = test_df.drop(['Item_Identifier', 'Outlet_Identifier'], axis = 1)

        file.write("\n\nPercentage of missing values - TRAIN: \n" + str((train_df.isnull().sum() / train_df.shape[0])*100))
        file.write("\n\nPercentage of missing values - TEST: \n" + str((test_df.isnull().sum() / test_df.shape[0])*100))

        #### UNIVARIATE ANALYSIS ###########

        for col in train_df.columns:
            if train_df[col].dtype in ['int64','float64']:
                Plotter_Helper.box_hist_plot(train_df[col],f"BigMart_Sales\\Plots\\histBox_{col}.png")
            elif train_df[col].dtype in ['object']:
                Plotter_Helper.barplot(train_df, col, f"BigMart_Sales\\Plots\\bar_{col}.png")



        ##### BIVARIATE ANALYSIS ###########
        Plotter_Helper.lineplot(train_df, x='Outlet_Establishment_Year',y='Item_Outlet_Sales'
                                ,save_path='BigMart_Sales\\Plots\\line_estYear_itemSales.png',estimator='mean')

        # Handle Missing Values


        ##### FEATURE ENGINEERING ###########


        ##### MODELING ######

            #Encode Categorical variables 

            #Scale Features 

            #Add constant 

            #OLS Modeling 

        end_time = datetime.now()
        file.write(f"\n\nEND ANALYSIS: {end_time}" )
        file.write("\nTIME TOOK: " + str((end_time - start_time).seconds) + " seconds.")
    