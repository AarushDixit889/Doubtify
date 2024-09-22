import PIL.Image
import streamlit as st
import google.generativeai as genai
import io

st.set_page_config("Doubtify")
st.title("Doubtify")
API_KEY=open("key.txt","r").read()
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel(model_name="gemini-1.5-flash")


uploaded_picture=st.file_uploader("")

if uploaded_picture is not None:
    st.image(uploaded_picture)
    image=PIL.Image.open(io.BytesIO(uploaded_picture.read()))
    st.write(model.generate_content(['Solve this question and also explain.',image]).text)
