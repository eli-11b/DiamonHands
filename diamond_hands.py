import pandas as pd
import streamlit as st
from datetime import date
from datetime import datetime
import yfinance as yf

st.write("""
# Diamond Hands: Stock Price App
Enter your information in the sidebar to the left. The rest we will do!
""")

#To the moon image in my local folder
st.image("/Users/Eli/Downloads/Moonshot.png")

#Today's date
today = date.today()

#create a side bar text entry that allows the user to enter the ticker.
ticker = st.sidebar.text_input("Input Stock Ticker")

#create side bar date_input objects so that the user can select start and end dates. 
beginning_date = st.sidebar.date_input("Choose your beginning date")
end_date = st.sidebar.date_input("Choose your end date")


#retrieve the data for that ticker
tickerdata = yf.Ticker(ticker)
tickerDf = tickerdata.history(period='1y',start=beginning_date, end=end_date)

# Typically the information you will get is Open, High, Low, 
# Close, Volume, and Dividends

#Open
st.subheader("Open")
st.write(tickerDf.Open[-1])
st.line_chart(tickerDf.Open)

#High
st.subheader("High")
st.write(tickerDf.High[-1])
st.line_chart(tickerDf.High)

#Low
st.subheader("Low")
st.write(tickerDf.Low[-1])
st.line_chart(tickerDf.Low)

#Close
st.subheader("Close")
st.write(tickerDf.Close[-1])
st.line_chart(tickerDf.Close)

#Volume
st.subheader("Volume")
st.write(tickerDf.Volume[-1])
st.line_chart(tickerDf.Volume)

#Dividends
st.subheader("Dividends")
st.write(tickerDf.Dividends[-1])
st.line_chart(tickerDf.Dividends)





