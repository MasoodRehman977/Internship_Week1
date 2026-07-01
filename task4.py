import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

country_sales = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

print(country_sales.head(10))

plt.figure(figsize=(12,6))
country_sales.head(10).plot(kind='bar')
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()