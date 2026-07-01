import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

numeric = df.select_dtypes(include=np.number)

plt.figure(figsize=(8,6))
sns.heatmap(numeric.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()