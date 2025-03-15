from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer,mean_squared_error, r2_score, mean_absolute_error

import statsmodels.api as sm
import numpy as np
import pandas as pd

class RegressModels:
    
    ### MODELS

    def build_and_fit_OLS(self, endog, exdog):

        ols_model = sm.OLS( endog, exdog)
        ols_res = ols_model.fit()

        return ols_model, ols_res
    
  


    def build_and_fit_RandomTree(self, x_train, y_train, x_test, y_test
                                  ,random_state = 1, rf_params ={}
                                  , scoring = "neg_mean_squared_error", cv=5):
        rf = RandomForestRegressor(random_state=random_state)

        grid_obj = GridSearchCV(rf, rf_params, scoring-scoring, cv=cv)
        grid_obj = grid_obj.fit(x_train, y_train)

        #set the RF_tuned regressor to the best combination of params
        rf_tuned = grid_obj.best_estimator_
        rf_tuned.fit(x_train, y_train)

        rf_tuned_test = self.model_performance_regression(rf_tuned, x_test, y_test)

        return rf, rf_tuned, rf_tuned_test
    
    ### METRICS

    """
        Function to compute different metrics to check regression model performance

        model: regressor
        predictors: independent variables
        target: dependent variable
    """
    
    def model_performance_regression(self, model, predictors, target):
      

        pred = model.predict(predictors)                  # Predict using the independent variables
        r2 = r2_score(target, pred)                       # To compute R-squared
        adjr2 = self.adj_r2_score(predictors, target, pred)    # To compute adjusted R-squared
        rmse = np.sqrt(mean_squared_error(target, pred))  # To compute RMSE
        mae = mean_absolute_error(target, pred)           # To compute MAE
        mape = self.mape_score(target, pred)                   # To compute MAPE

        # Creating a dataframe of metrics
        df_perf = pd.DataFrame(
            {
                "RMSE": rmse,
                "MAE": mae,
                "R-squared": r2,
                "Adj. R-squared": adjr2,
                "MAPE": mape,
            },
            index=[0],
        )

        return df_perf
    
    # Helper Function to compute adjusted R-squared
    def adj_r2_score(self, predictors, targets, predictions):
        r2 = r2_score(targets, predictions)
        n = predictors.shape[0]
        k = predictors.shape[1]
        return 1 - ((1 - r2) * (n - 1) / (n - k - 1))


    # Helper Function to compute MAPE
    def mape_score(self, targets, predictions):
        return np.mean(np.abs(targets - predictions) / targets) * 100