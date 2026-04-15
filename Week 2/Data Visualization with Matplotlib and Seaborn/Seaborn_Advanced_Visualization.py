import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = np.random. rand(5, 5)
print(data)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("HeatMap")
plt.show()

df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()

sns.boxplot(df)
plt.show()
