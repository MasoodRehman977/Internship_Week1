import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Quantity'])
plt.title("Boxplot of Quantity")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Price'])
plt.title("Boxplot of Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Revenue'])
plt.title("Boxplot of Revenue")
plt.show()