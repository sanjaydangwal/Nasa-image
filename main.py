import streamlit as st
import requests
import os
from PIL import Image

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)

response_dict = response.json()
img = Image.open(requests.get(response_dict["hdurl"], stream=True).raw)

st.set_page_config(layout="wide")
st.title(response_dict["title"])
st.image(img)
st.write(response_dict["explanation"])
