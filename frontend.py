# frontend.py
import streamlit as st
import sys
import os
import matplotlib as plt

st.title("Welcome to Classify!")
st.text("i swear it sounds familiar")

with st.sidebar:
    st.header("Upload the Song")
    uploaded_file = st.file_uploader("Upload in MP4 or WAV", type = ['MP4','WAV'])

    use_sample = st.file_uploader("Use Sample file")

    if use_sample:
        file_path = ""
    else:
        file_path = None
