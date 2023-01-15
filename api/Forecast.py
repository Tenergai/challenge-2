import math
import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


class Forecast:
    def __init__(self):
        df = pd.read_csv('../datasetFinal.csv')

        y = df['generated_power']
        X = df.drop(columns='generated_power')

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.2)

        self.model = RandomForestRegressor()
        self.model.fit(self.x_train,self.y_train)

    def train_svm(self):
        self.model = Pipeline([
            ("scaler", StandardScaler()),
            ("svm_reg", SVR(C=276.71078708,epsilon = 1, gamma = 0.28109356)),
        ])

        self.model.fit(self.x_train,self.y_train)

        y_pred_svm = self.model.predict(self.x_test)
        mae_svm = mean_absolute_error(y_pred_svm, self.y_test)
        rmse_svm = math.sqrt(mean_squared_error(y_pred_svm,self.y_test))
        score_svm = self.model.score(self.x_test,self.y_test)
        return score_svm
    
    def train_rf(self):
        self.model = RandomForestRegressor()
        self.model.fit(self.x_train,self.y_train)
        y_pred_rf = self.model.predict(self.x_test)
        mae_rf = mean_absolute_error(y_pred_rf, self.y_test)
        rmse_rf = math.sqrt(mean_squared_error(y_pred_rf,self.y_test))
        score_rf = self.model.score(self.x_test,self.y_test)
        return score_rf

    def train_dt(self):
        self.model = DecisionTreeRegressor(criterion ="friedman_mse", max_depth=10, 
                                    min_samples_split=10, random_state=5)
        self.model.fit(self.x_train,self.y_train)
        y_pred_dt = self.model.predict(self.x_test)
        mae_dt = mean_absolute_error(y_pred_dt, self.y_test)
        rmse_dt = math.sqrt(mean_squared_error(y_pred_dt,self.y_test))
        score_dt = self.model.score(self.x_test,self.y_test)
        return score_dt

    def predict(self,day):
        #d = self.scaler.transform(day)
        return self.model.predict(day).tolist()
