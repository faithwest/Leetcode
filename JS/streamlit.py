import streamlit as st
import requests

# Set the title of the app
st.title('Cat Web App')

# Display a welcome message
st.write('Welcome to the Cat Web App!')

# Display a cat picture
cat_image_url = "https://placekitten.com/400/300"
st.image(cat_image_url, caption='Cute Cat')

# Fetch and display cat facts
st.write('Here are some interesting facts about cats:')

response = requests.get('https://catfact.ninja/fact')
if response.status_code == 200:
    cat_fact = response.json().get('fact')
    st.write(f'- {cat_fact}')
else:
    st.write('Unable to fetch cat facts at the moment.')


import streamlit as st
import yfinance as yf

# Get user input for stock symbol
ticker_symbol = st.text_input("Enter Stock Ticker Symbol:")

# Download stock data (if symbol is valid)
if ticker_symbol:
  try:
    stock_data = yf.download(ticker_symbol)
  except Exception as e:
    st.error(f"Error downloading data for {ticker_symbol}: {e}")
    stock_data = None

# Display stock information (if data downloaded successfully)
if stock_data is not None:
  st.write(f"## Stock Information for {ticker_symbol}")
  st.write(f"Company Name: {stock_data['shortName'].values[0]}")
  st.write(f"Current Price: ${stock_data['Close'].iloc[-1]}")

  # Plot closing price over time
  st.line_chart(stock_data['Close'])

# Display message if no symbol is entered
if not ticker_symbol:
  st.warning("Please enter a stock ticker symbol.")

