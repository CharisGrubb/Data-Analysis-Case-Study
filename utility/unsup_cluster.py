from scipy.spatial.distance import cdist, pdist
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd


class Cluster_Helper:

    @classmethod 
    def scaler(cls):
        pass

    @classmethod 
    def PCA(cls, scaled_df, n_comps, random_state = 1):
        pca = PCA(n_components=n_comps, random_state=random_state)
        data_pca = pca.fit_transform(scaled_df)
        exp_var = (pca.explained_variance_ratio_)

        return data_pca, exp_var

    @classmethod 
    def k_means_clustering(cls, pca_data, k, random_state = 1, n_init="auto"):
        pca_data_copy = pca_data.copy()
        model = KMeans(n_clusters = k, random_state =random_state, n_init = n_init)
        model.fit(pca_data)
        prediction = model.predict(pca_data_copy)

        distortion = (sum(np.min(cdist(pca_data_copy, model.cluster_centers_, "euclidean"), axis = 1))/pca_data_copy.shape[0])
        
        
        return distortion, prediction, model


    @classmethod 
    def gaussian_mix_clustering(cls):
        pass

    @classmethod
    def get_silhouette_score(cls):
        pass