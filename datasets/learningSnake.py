import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
def find_model_perf(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_hat = [x[1] for x in model.predict_proba(X_test)]
    auc = roc_auc_score(y_test, y_hat)

    return auc
df = pd.read_csv('D:\\f4itech\\challenge-2\\datasets\\datasetFinal.csv')
df.drop('generated_power', axis=1)

X = df.drop('generated_power', axis=1)
y = df['generated_power']
#clf = tree.DecisionTreeRegressor()


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.70, random_state=1)



print(find_model_perf(X_train, X_test, y_train, y_test))
#clf = clf.fit(X, y)
#clf.predict([[1, 1]])