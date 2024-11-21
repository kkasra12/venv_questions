import pandas as pd
import matplotlib.pyplot as plt

data = {'values': [1, 2, 2, 3, 3, 3, 4, 4]}
df = pd.DataFrame(data)
df['values'].hist()
plt.show()
