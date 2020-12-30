import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

#Importing the csv file and choosing the X and Y variables
df = pd.read_csv("auto_dataset.csv")
X = df["weight"]
Y = df["horsepower"]
X = X.values.reshape(-1,1)
Y = Y.values.reshape(-1,1)

reg.fit(X, Y)
print("The value obtained for beta_o is: ", reg.intercept_)
print("The value obtained for beta_1 is: ",reg.coef_)

X_new = np.array([[2500],[2045]])
print(reg.predict(X_new))
