import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first sheet
df = pd.read_excel("online_retail_II.xlsx")

plt.figure(figsize=(10,6))
sns.histplot(df['Revenue'], bins=50)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()