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
