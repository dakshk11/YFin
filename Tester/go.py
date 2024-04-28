import yfinance as yf

msft = yf.Ticker("MSFT")

ned = msft.news

print(ned)