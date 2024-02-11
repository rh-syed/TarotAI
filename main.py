import streamlit as st
import tarot

st.title("Unlock the Secrets of Your Future with IntuiTarot")
question = st.text_area(label="What is your question?")
button = st.button("Ask My Spirit Guides")
if button and question:
    st.text("Consulting your spirit guides...hang tight...")
    response = tarot.consultTarot(question)
    st.text("")
    st.text(response)
