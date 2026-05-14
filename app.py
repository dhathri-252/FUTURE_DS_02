import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/customer_churn.csv")

# Title
st.title("Customer Retention & Churn Analysis Dashboard")

# Metrics
total_customers = len(df)
churned = df[df["Churn"] == "Yes"].shape[0]
retained = df[df["Churn"] == "No"].shape[0]

retention_rate = (retained / total_customers) * 100
churn_rate = (churned / total_customers) * 100

# KPI Section
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Churned", churned)
col3.metric("Retention Rate", f"{retention_rate:.2f}%")
col4.metric("Churn Rate", f"{churn_rate:.2f}%")

# Dataset Preview
st.subheader("Customer Dataset")
st.write(df)

# Churn Distribution Bar Chart
st.subheader("Churn Distribution")

churn_data = df["Churn"].value_counts()

fig, ax = plt.subplots()
ax.bar(churn_data.index, churn_data.values)

st.pyplot(fig)

# Pie Chart
st.subheader("Customer Retention Pie Chart")

fig2, ax2 = plt.subplots()
ax2.pie(
    churn_data.values,
    labels=churn_data.index,
    autopct="%1.1f%%"
)

st.pyplot(fig2)

# Subscription Analysis
st.subheader("Subscription Type Analysis")

subscription = df.groupby("SubscriptionType")["Churn"].value_counts()

st.write(subscription)

# Monthly Charges Analysis
st.subheader("Monthly Charges Analysis")

fig3, ax3 = plt.subplots()
ax3.plot(df["MonthlyCharges"])

st.pyplot(fig3)