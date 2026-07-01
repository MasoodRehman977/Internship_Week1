import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

# If it gives sheet error, use:
# df = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2009-2010")

df.head()

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nInformation:")
df.info()

df.describe(include='all')

missing = df.isnull().sum()

print("Missing Values")
print(missing)

plt.figure(figsize=(10,5))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)