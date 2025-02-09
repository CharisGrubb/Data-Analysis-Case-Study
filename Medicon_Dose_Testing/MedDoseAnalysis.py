from utility.plotter import Plotter_Helper
import numpy as np
import pandas as pd


def analyze():

    df = pd.read_csv("Medicon_Dose_Testing\\doses.csv")

    print(df.info())