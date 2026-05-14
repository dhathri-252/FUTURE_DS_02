import pandas as pd

# Load dataset
df = pd.read_csv("../data/customer_churn.csv")

# Show first rows
print(df.head())

# Total customers
print("Total Customers:", len(df))

# Churn count
print(df["Churn"].value_counts())

# Average monthly charges
print("Average Monthly Charges:", df["MonthlyCharges"].mean())

# Subscription churn analysis
print(df.groupby("SubscriptionType")["Churn"].value_counts())