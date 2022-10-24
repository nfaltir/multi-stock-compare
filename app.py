import streamlit as st
import pandas as pd
import base64
import matplotlib as plt
import yfinance as yf
import csv

st.set_page_config(page_title="Stonks", page_icon="🌱")
st.markdown("<h1 style='text-align: center; color: #5837D0;'>Stock Comparison</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-weight: lighter; color: #FF8243; '><strong><a style='text-decoration: none; color: #749F82;' target='_blank' href='https://github.com/nfaltir/multi-stock-compare'>Github</a></strong></h4>", unsafe_allow_html=True)
st.write("-------------------------------------------------------- ")


file = open('nasdaq.csv')
tickers = (pd.read_csv(file))


start = st.date_input('Select Start', value = pd.to_datetime('2020-01-01'))
end = st.date_input('Select End', value = pd.to_datetime('today'))
stock_options = st.multiselect("Pick or Enter a Stock Ticker(s):", tickers)


def relative_return(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


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
  


