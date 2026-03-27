import streamlit as st
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

st.title("Project 1 - AI Trading Bot with Quant Backtesting")
st.subheader("Day 1: Live Market data fetcher")

#Fetch data
ticker = st.selectbox("Choose Crypto to Fetch:", ["BTC-USD", "XRP-USD"]);
data = yf.download(ticker, period="30d")

st.write("Last 5 rows of data:")
st.dataframe(data.tail())

#Simple plot
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'])
ax.set_title(f"{ticker} Closing Price - Last 30 Days")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
fig.autofmt_xdate()
st.pyplot(fig)

st.write("✅ First day target achieved")