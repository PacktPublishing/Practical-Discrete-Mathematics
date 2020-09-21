import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importing the csv file and choosing the X and Y variables
df = pd.read_csv("auto_dataset.csv")
print(df.shape)

X = df["weight"]
Y = df["horsepower"]

X_b = np.c_[np.ones((392,1)),X] #add X_o = 1 to each instance
beta_values = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)

X_new = np.array([[2500],[2045]])
X_new_b = np.c_[np.ones((2,1)),X_new]
y_predict = X_new_b.dot(beta_values)
print("Weight of car = 2500; predicted horsepower is {:.1f}; actual horsepower is 88".format(y_predict[0]))
print("Weight of car = 2045; predicted horsepower is {:.1f}; actual horsepower is 68".format(y_predict[1]))
#
X_plot= np.array([[1500],[6000]])
X_plot_b = np.c_[np.ones((2,1)),X_plot]
Y_plot = X_plot_b.dot(beta_values)

Equationline = "Y ={:.3f}+{:.3f}X".format(beta_values[0], beta_values[1])
plt.plot(X_plot, Y_plot, "r-", label = Equationline)
sns.scatterplot(X,Y, label = "Training Data")
plt.legend()
plt.show()