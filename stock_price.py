
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

stock_symbol = 'AAPL'  
end_date = datetime.now()
start_date = end_date - timedelta(days=30) 

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

plt.figure(figsize=(10, 5))
plt.plot(stock_data['Close'], marker='o', linestyle='-', color='b', markersize=5, label=stock_symbol)
plt.title(f'Cute Stock Price Graph for {stock_symbol}', fontsize=16, color='purple')
plt.xlabel('Date', fontsize=12, color='green')
plt.ylabel('Closing Price (USD)', fontsize=12, color='green')
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='pink')
plt.axhline(y=stock_data['Close'].mean(), color='r', linestyle='--', linewidth=1, label='Mean Price')
plt.legend()

plt.annotate('Start', xy=(stock_data.index[0], stock_data['Close'][0]), xytext=(stock_data.index[5], stock_data['Close'][0] + 5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='orange')
plt.annotate('End', xy=(stock_data.index[-1], stock_data['Close'][-1]), xytext=(stock_data.index[-10], stock_data['Close'][-1] - 5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='orange')

plt.tight_layout()
plt.show()
