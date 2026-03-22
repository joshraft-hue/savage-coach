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
# Grok setup - REPLACE WITH YOUR KEY\
client = OpenAI(\
\'a0\'a0\'a0\'a0api_key="xai-FEfNEGfaxARLoCygpMuCDve2vTY1eVfLLxDgXIhHN4VUobBDLhVglVKqoICnLxM6gjoYZ87TkrQZeNOY",\'a0\'a0# PASTE YOUR GROK KEY\
\'a0\'a0\'a0\'a0base_url="https://api.x.ai/v1"\
)\
\
st.set_page_config(page_title="Absolute Savage Coach", layout="wide")\
st.markdown("### \uc0\u55357 \u56448  ABSOLUTE SAVAGE COACHING \u55357 \u56448 ")\
\
# Sidebar Tracker\
with st.sidebar:\
\'a0\'a0\'a0\'a0st.header("EMPIRE METRICS")\
\'a0\'a0\'a0\'a0calories = st.number_input("Calories", value=965)\
\'a0\'a0\'a0\'a0protein = st.number_input("Protein (g)", value=66.8)\
\'a0\'a0\'a0\'a0liquids = st.number_input("Liquids (L)", value=0.5)\
\'a0\'a0\'a0\'a0if st.button("ROAST ME NOW"):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0st.balloons()\
\
# Chat History\
if "messages" not in st.session_state:\
\'a0\'a0\'a0\'a0st.session_state.messages = [\{"role": "system", "content": "You are Absolute Savage Coach\'97Goggins/Jocko drill sergeant style. Politically incorrect HARD truths. Track fitness/nutrition, ROAST failures, demand PRs. End every response BOATS! \uc0\u55357 \u56448 "\}]\
\
for msg in st.session_state.messages:\
\'a0\'a0\'a0\'a0st.chat_message(msg["role"]).markdown(msg["content"])\
\
if prompt := st.chat_input("Log food/gym or ask savage advice..."):\
\'a0\'a0\'a0\'a0st.session_state.messages.append(\{"role": "user", "content": prompt\})\
\'a0\'a0\'a0\'a0st.chat_message("user").markdown(prompt)\
\'a0\'a0\'a0\'a0\
\'a0\'a0\'a0\'a0with st.chat_message("assistant"):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0response = client.chat.completions.create(\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0model="grok-beta",\'a0\'a0# Or grok-2-latest\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0messages=st.session_state.messages\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0).choices[0].message.content\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0st.markdown(response)\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0st.session_state.messages.append(\{"role": "assistant", "content": response\})}