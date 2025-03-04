import statsmodels.api as sm



class LinReg:
    
    
    def build_and_fit_OLS(self, endog, exdog):

        ols_model = sm.OLS( endog, exdog)
        ols_res = ols_model.fit()

        return ols_model, ols_res