import pandas as pd

customer_df = pd.read_csv("C:/Users/anipb/Desktop/CustomerList.csv")

print(customer_df)

print("Example for AND operator")
print(customer_df.loc[(customer_df['Country'] == 'USA') & (customer_df['State'] == 'Georgia')])

print("Example for OR operator")
print(customer_df.loc[(customer_df['Country'] == 'USA') | (customer_df['State'] == 'Ontario')])

print("Example for NOT operator")
print(customer_df.loc[(customer_df['Country'] != 'USA')])