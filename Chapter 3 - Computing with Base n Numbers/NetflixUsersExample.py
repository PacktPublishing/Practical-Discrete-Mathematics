# Import the pandas library
import pandas as pd

# Read the provided customer data CSV file
customer_df = pd.read_csv("C:/Users/anipb/Desktop/CustomerList.csv")

# Display the customer data
print(customer_df)

# Find customers from Georgia and from the USA
print("Example for AND operator")
print(customer_df.loc[(customer_df['Country'] == 'USA') & (customer_df['State'] == 'Georgia')])

# Find customers from the USA or from Ontario
print("Example for OR operator")
print(customer_df.loc[(customer_df['Country'] == 'USA') | (customer_df['State'] == 'Ontario')])

# Find customers who are not from the USA
print("Example for NOT operator")
print(customer_df.loc[(customer_df['Country'] != 'USA')])