import streamlit as st
import requests

# Set up the page
st.set_page_config(page_title="Pet App", page_icon="🐾")

st.header("Welcome to My Pet App", divider="rainbow")

# Function to get a cat image
def get_cat_image():
    url = "https://cataas.com/cat"
    contents = requests.get(url)
    return contents.content

# Function to get a dog image URL
def get_dog_image_url():
    url = "http://random.dog/woof.json"
    contents = requests.get(url).json()
    # Use the correct key "url" to get the image URL
    dog_image_url = contents.get("url")
    return dog_image_url

# Create two columns
c1, c2 = st.columns(2)

# Cat image button in the first column
with c1:
    cat_button = st.button("Click here for a cat image")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="My Cat Image")

# Dog image button in the second column
with c2:
    dog_button = st.button("Click here for a dog image")
    if dog_button:
        dog_image_url = get_dog_image_url()
        if dog_image_url:  # Check if the URL is valid
            st.image(dog_image_url, width=300, caption="My Dog Image")

