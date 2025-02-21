from scipy.spatial.distance import cdist, pdist
from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from utility import plotter
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


def analyze():


    data = pd.read_csv("Fantasy_Sports_Clustering\\fpl_data.csv")
    data_copy = data.copy() #Copy in order to maintain original data for reference

    dup_sum = data_copy.duplicated().sum() 

    print(dup_sum)