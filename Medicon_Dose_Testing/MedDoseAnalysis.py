from utility.plotter import Plotter_Helper
from scipy.stats import binom, norm,stats
import numpy as np
import pandas as pd


def analyze():
    with open('Medicon_Dose_Testing\\analysis_output.txt','w') as file:
        
        df = pd.read_csv("Medicon_Dose_Testing\\doses.csv")
        print(df)
        
        #As we already know, the quality assurance team checked on 
        # five batches of doses and found that - it is 10 times more likely
        # that a dose will be able to produce a satisfactory result than 
        # not. So, the probability that a dose will do a satisfactory job is 10p
        # so if p+10p=1 (according to the rules of probability), probability is:
        p = 0.09 #(1/11) #Probability that a dose will NOT do a satisfactory job
        n = 100 #Sample size
        k = np.arange(0, n+1)
        
        mu = df['time_of_effect'].mean()
        sigma = df['time_of_effect'].std()

        binomials = binom.pmf(k=k, n=n, p=p) #Probability Mass Function because this is a DISCRETE statistics problem
        file.write(f"Probability/MU(mean)/Sigma(standard deviation): {p}/{mu}/{sigma} \n\n")
        file.write(f"Binomials for trials 0 to {n}:\n {binomials} \n\n" )


        file.write("DATASET INFO: \n")
        file.write(str(df.info()))

 