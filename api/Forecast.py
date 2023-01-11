import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class Forecast:
    def __init__(self):
        df = pd.read_csv('./datasetFinal.csv')
        """ self.scaler = StandardScaler()
        names = df.columns
        d = self.scaler.fit_transform(df)
        df = pd.DataFrame(d, columns = names) """

        y = df['generated_power']
        X = df.drop(columns='generated_power')

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.2)

        self.model = SVR(C=1.59041293, epsilon=0.1, gamma = 1)

        self.model.fit(self.x_train,self.y_train)

        self.score = self.model.score(self.x_test,self.y_test)

    def predict(self,day):
        #d = self.scaler.transform(day)
        return self.model.predict(day).tolist()

