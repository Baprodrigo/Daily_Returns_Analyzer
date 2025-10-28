## Daily Returns & Volatility Analyzer

This is A beginner-friendly quant finance project that fetches stock price data, computes daily returns, cumulative growth, and rolling volatility — then visualizes them beautifully. 

This project introduces essential tools for analyzing and visualizing financial time-series data using Python, pandas, and yfinance.

### 🧠 What this project does 

- ✅ Downloads historical price data for multiple assets (via Yahoo Finance) 
- ✅ Calculates daily returns (arithmetic) 
- ✅ Computes cumulative growth of $1 invested 
- ✅ Estimates rolling volatility (21-day window) and annualizes it 
- ✅ Generates and saves clear plots of growth & volatility 
- ✅ Teaches data hygiene and reproducibility best practices for quants.

### Key Concepts Learned

| Concept                           | Why it matters in finance                                              |
| --------------------------------- | ---------------------------------------------------------------------- |
| **APIs & data ingestion**         | Every quant pipeline starts with clean, automated data collection.     |
| **Adjusted close prices**         | Reflect total return (splits/dividends). Always use them for accuracy. |
| **Returns & compounding**         | Normalize performance across assets; measure growth properly.          |
| **Rolling volatility**            | Risk is time-varying — rolling windows show volatility clusters.       |
| **Annualization (√252)**          | Compare daily metrics on a consistent yearly scale.                    |
| **Visualization**                 | Good plots tell better stories than raw tables.                        |
| **Reproducible folder structure** | Separating `/data` and `/figures` = professional workflow.             |

### Requirements

Install dependencies (inside your virtual environment):

pip install yfinance pandas numpy matplotlib

### 🚀 How to Run

- Clone this repo or copy the code into a PyCharm project.

- Run analyzer.py.

- Wait a few seconds — data will download and plots will appear.

- Check your /figures folder for:

    - cumulative_returns.png

    - rolling_volatility.png

### Author

Rodrigo Baptista
Quant finance enthusiast | Business Management student | LearnMate CFO
[LinkedIn Profile](https://www.linkedin.com/in/rodrigosbaptista/)


