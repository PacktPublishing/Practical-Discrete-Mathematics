import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importing the csv file
df = pd.read_csv("auto_dataset.csv",index_col=0)
print(df.head())

#Plotting the pairplot
sns.pairplot(df, diag_kind="kde")
plt.show()