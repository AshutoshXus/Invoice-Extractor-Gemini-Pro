from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    response  = model.generate_content([input,image])
    return response.text


st.set_page_config(page_title="Multilanguage Invoice Extraction")
input = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose image of the invoce....", type=["jpg",'jpeg','png'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)


submit = st.button("Tell me about invoce")

input_prompt = """ You are an expert understanding invoices. We will upload an image as invoice you will have to answer any question based on 
uploaded invoice. 
"""

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Resposne is")
    st.write(response)




