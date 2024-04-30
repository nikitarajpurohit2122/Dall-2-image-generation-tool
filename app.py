from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

client = OpenAI(api_key=apikey)

single_img=dict(
        title="",
        text="",
        interval=None,
        img="",
    )
def generate_images(image_description, num_image):
    
    image_gallary=[]
    
    for i in range (num_image):
        img_response = client.images.generate(
            model="dall-e-2",
            prompt=image_description,
            size="512x512",
            quality="standard",
            n=1
        )
        
        image_url = img_response.data[0].url
        new_image=single_img.copy()
        new_image["title"] = f"Image {i+1}"
        new_image["text"]=image_description
        new_image["img"]=image_url
        
        image_gallary.append(new_image)
    return image_gallary
st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")

st.title("DALL-E-2 Image Generation Tool")

st.subheader("POWERED BY THE WORLD's MOST POWERFUL Image Generator API- DALL-E")
img_description = st.text_area("Enter a description for the image you want to generate")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=10, value=1)

if st.button("Generate Images"):
    generated_images = generate_images(img_description, num_of_images)    
    carousel(items=generated_images, width=1)