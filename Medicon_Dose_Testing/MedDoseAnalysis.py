from utility.plotter import Plotter_Helper
from scipy.stats import binom, norm,stats
import numpy as np
import pandas as pd


def analyze():

    df = pd.read_csv("Medicon_Dose_Testing\\doses.csv")

    p = 0.09 #(1/11)


    mu = df['time_of_effect'].mean()
    sigma = df['time_of_effect'].std()