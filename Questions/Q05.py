import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
data['Close'].plot()
plt.show()

