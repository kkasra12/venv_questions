import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
'x': [1, 2, 3, 4],
'y': [10, 15, 7, 20]
})

sns.lineplot(data=df, x='x', y='y')
plt.show()
