import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")
plt.rcParams["figure.figsize"]=(10,5)

os.makedirs ("data", exist_ok=True)
os.makedirs ("figures", exist_ok=True)

tickers = [ "NVDA", "IBKR", "PLTR"]
start = "2020-01-01"
data = yf.download(
    tickers, start=start, auto_adjust=False, progress=False
)

if isinstance(data.columns, pd.MultiIndex):
    px = data["Adj Close"].dropna (how="all")
else:
    px = data["Adj Close"].to_frame().dropna(how="all")

data.to_csv("data/prices.csv")

returns = data.pct_change().dropna()
cumulative = (1+ returns).cumprod()

rolling_vol = returns.rolling(21).std() * np.sqrt(252)

cumulative.plot(title="Cumulative Growth of $1")
plt.ylabel("Growth")
plt.tight_layout()
plt.savefig("figures/cumulative_returns.png")
plt.show()

rolling_vol.plot(title="Rolling 21D Annualized Volatility")
plt.ylabel("Volatility")
plt.tight_layout()
plt.savefig("figures/rolling_volatility.png")
plt.show()

print("Analysis Complete! Check your 'figures' folder for your charts. ")