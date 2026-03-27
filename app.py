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