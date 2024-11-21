import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3]])
y = np.array([2, 3, 5])
model = LinearRegression().fit(X, y)
print(model.coef_, model.intercept_)
