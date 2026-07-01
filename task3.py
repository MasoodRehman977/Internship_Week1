import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

df['Revenue'] = df['Quantity'] * df['Price']

df[['Quantity','Price','Revenue']].head()

top_quantity = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

print(top_quantity)

plt.figure(figsize=(12,6))
top_quantity.plot(kind='bar')
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=75)
plt.show()

top_revenue = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

print(top_revenue)

plt.figure(figsize=(12,6))
top_revenue.plot(kind='bar', color='green')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=75)
plt.show()

country_sales = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

print(country_sales.head(10))

plt.figure(figsize=(12,6))
country_sales.head(10).plot(kind='bar')
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(14,6))
monthly_sales.plot(marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
