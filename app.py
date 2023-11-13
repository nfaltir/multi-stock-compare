import streamlit as st
import pandas as pd
import base64
import matplotlib as plt
import yfinance as yf
import csv

st.set_page_config(page_title="Stonks", page_icon="🌱")
st.markdown("<h1 style='text-align:center; border-radius:10px; color:white; font-size:64px;'>Stock Performance</h1>", unsafe_allow_html=True)
st.write("-------------------------------------------------------- ")


file = open('data/stocks.csv')
tickers = (pd.read_csv(file))


stock_options = st.multiselect("Enter a Stock Ticker(s):", tickers)

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Add content to the first column
with col1:
    st.write("")
    start = st.date_input('Select Start', value = pd.to_datetime('2020-01-01'))

# Add content to the second column
with col2:
    st.write("")
    st.write("")

with col3:
    st.write("")
    end = st.date_input('Select End', value = pd.to_datetime('today'))




def relative_return(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

st.write("-------------------------------------------------------- ")
if len(stock_options) > 0:

    closingPrice = yf.download(stock_options,start,end)['Adj Close']
    stock_returns = relative_return(yf.download(stock_options,start,end)['Adj Close']) 
    volume = yf.download(stock_options,start,end)['Volume']
   
    st.write("### Closing Price")
    st.line_chart(closingPrice)
    
    st.write("### Returns")
    st.area_chart(stock_returns)
    st.write("### Volume")
    st.bar_chart(volume)
  

st.markdown("<h4 style='text-align: center; margin-top:400px; font-weight: light;'><strong><a style='text-decoration: none; color:salmon;' target='_blank' href='https://github.com/nfaltir/multi-stock-compare'>GITHUB ⚙️</a></strong></h4>", unsafe_allow_html=True)
