{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNS-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf0 import streamlit as st\
from openai import OpenAI\
import os\
\
# SECURE: Key from Streamlit Secrets\
client = OpenAI(\
\'a0\'a0\'a0\'a0api_key=os.getenv("XAI_API_KEY"),\
\'a0\'a0\'a0\'a0base_url="https://api.x.ai/v1"\
)\
\
st.set_page_config(page_title="Absolute Savage Coach", layout="wide")\
st.markdown("### \uc0\u55357 \u56448  ABSOLUTE SAVAGE COACHING \u55357 \u56448 ")\
\
with st.sidebar:\
\'a0\'a0\'a0\'a0st.header("EMPIRE METRICS")\
\'a0\'a0\'a0\'a0st.number_input("Calories", value=965)\
\'a0\'a0\'a0\'a0st.number_input("Protein g", value=66.8)\
\'a0\'a0\'a0\'a0st.number_input("Liquids L", value=0.5)\
\'a0\'a0\'a0\'a0if st.button("ROAST ME"):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0st.balloons()\
\
if "messages" not in st.session_state:\
\'a0\'a0\'a0\'a0st.session_state.messages = [\{"role": "system", "content": "Goggins savage coach: HARD truths, ROAST failures, demand gym. End BOATS! \uc0\u55357 \u56448 "\}]\
\
for msg in st.session_state.messages:\
\'a0\'a0\'a0\'a0st.chat_message(msg["role"]).markdown(msg["content"])\
\
if prompt := st.chat_input("Log food/gym..."):\
\'a0\'a0\'a0\'a0st.session_state.messages.append(\{"role": "user", "content": prompt\})\
\'a0\'a0\'a0\'a0st.chat_message("user").markdown(prompt)\
\'a0\'a0\'a0\'a0response = client.chat.completions.create(\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0model="grok-beta",\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0messages=st.session_state.messages\
\'a0\'a0\'a0\'a0).choices[0].message.content\
\'a0\'a0\'a0\'a0st.session_state.messages.append(\{"role": "assistant", "content": response\})\
\'a0\'a0\'a0\'a0st.chat_message("assistant").markdown(response)}