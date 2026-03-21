import streamlit as st
import openai
from datetime import datetime
import os

openai.api_key = "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"  # REPLACE THIS WITH YOUR KEY FROM STEP 3

st.set_page_config(page_title="Absolute Savage Coach", layout="wide")
st.markdown("### 💀 ABSOLUTE SAVAGE COACHING 💀")

with st.sidebar:
    st.header("EMPIRE TRACKER")
    calories = st.number_input("Calories", value=965)
    protein = st.number_input("Protein g", value=66.8)
    carbs = st.number_input("Carbs g", value=65.8)
    fat = st.number_input("Fat g", value=43.1)
    liquids = st.number_input("Liquids L", value=0.5)
    if st.button("ROAST ME"):
        st.balloons()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Unhinged Goggins coach: ROAST HARD truths on macros/gym. End BOATS! 💀"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Log food/gym or ask advice"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    ).choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
