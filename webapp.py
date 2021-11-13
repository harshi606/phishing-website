# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import sklearn
import pickle

#loading the model

pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
st.title('Phish-find')

nav = st.sidebar.radio("Navigate",["Home","Prediction"])

if nav == "Home":
    st.image("img.jpg",width=800)
if nav == "Prediction":
    st.write("pred")
    website = st.text_input("WEBSITE")
    op = classifier.predict([website])
    if op == 0:
        st.write("It is Phishing ! Stay away !")
    else:
        st.write("Legitimate website ! You are safe to proceed!")
        
    


st.write("Paste the website url")


