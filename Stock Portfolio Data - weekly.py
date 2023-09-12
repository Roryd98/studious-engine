#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import pandas as pd

# List of stock symbols
stock_symbols = ["TSLA", "AMZN", "NFLX", "NVDA", "SQ", "AMD", "ZM", "ELF", "MRNA", "DIS", "JPM", "JNJ", "CVX", "PG", "KO", "LUV", "CMG", "NOW", "URI", "FCX"]

# Function to get Friday closing prices and dates
def get_friday_closes_with_dates(stock_symbols):
    data_list = []

    for symbol in stock_symbols:
        try:
            # Fetch stock data using Yahoo Finance
            data = yf.download(symbol, period="182d", interval="1d")

            # Filter for Fridays (assuming last day of the week is Friday)
            friday_data = data[data.index.dayofweek == 4]

            # Extract dates and closing prices
            dates = friday_data.index.strftime("%Y-%m-%d")
            closes = friday_data["Close"].tolist()

            # Append data to the list
            data_list.extend(list(zip([symbol] * len(dates), dates, closes)))
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")

    return data_list

# Get Friday closing prices and dates for the list of stocks
data_list = get_friday_closes_with_dates(stock_symbols)

# Convert the result to a DataFrame
df = pd.DataFrame(data_list, columns=["Symbol", "Date", "Friday Close"])

# Pivot the DataFrame to have tickers as columns
pivot_df = df.pivot(index="Date", columns="Symbol", values="Friday Close")

# Reorder columns based on the original order of stock_symbols
desired_order = stock_symbols
pivot_df = pivot_df[desired_order]

# Save the pivoted DataFrame to an Excel (XLSX) file
pivot_df.to_excel("stock_friday_closes.xlsx")




# In[ ]:





# In[ ]:







# In[ ]:




