import streamlit as st
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

@st.cache(hash_funcs={transformers.models.gpt2.tokenization_gpt2_fast.GPT2TokenizerFast: hash}, suppress_st_warning=True)
def load_data():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model

st.set_page_config(page_title="Chatbot")
st.write("Welcome to the DialoGPT-medium chatbot example.")
tokenizer, model = load_data()

# Init Session State
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.chat_history_ids = None
    st.session_state.history = []
else:
    st.session_state.step+=1

input = st.text_input(label="Enter your question:")

if input:
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_user_input_ids], dim=-1) if st.session_state.step > 1 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    st.session_state.chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
    response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    st.session_state.history.append(input)
    st.session_state.history.append(response)

if st.button('Reset'):
    st.session_state.step = 0
    st.session_state.chat_history_ids = None
    st.session_state.history = []

for x in range(len(st.session_state.history)):
    person = "**User**" if x%2==0 else "**Bot**"
    st.write(person, st.session_state.history[x])
    
st.write("Step: ", st.session_state.step)
st.write(st.session_state.chat_history_ids)

