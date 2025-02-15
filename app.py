import streamlit as st
import json
import os
from datetime import datetime
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
import time  

# Hide Chat History
HISTORY_FILE = "chat_history.json"

# Loading Function of chat
def load_chat_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  

# Save chat history
def save_chat_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# Clear chat history
def clear_chat_history():
    st.session_state.message_log = []
    save_chat_history([])
    st.rerun()

# Set Page Theme(Night/Daytime Mode)
current_hour = datetime.now().hour

if 18 <= current_hour or current_hour < 6:
    background_color = "#1a1a1a"
    text_color = "#ffffff"
    sidebar_bg = "#2d2d2d"
    button_color = "#ff4444"
    button_text_color = "#ffffff"  
    input_background_color = "#2d2d2d"  
    input_text_color = "#ffffff"  
else:
    background_color = "#f5f5f5"
    text_color = "#333333"
    sidebar_bg = "#ffffff"
    button_color = "#d9534f"
    button_text_color = "#ffffff"  
    input_background_color = "#ffffff"  
    input_text_color = "#333333"  

# Night/Daytime Mode Style with CSS
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {background_color} !important;
            color: {text_color} !important;
        }}
        .stSidebar {{
            background-color: {sidebar_bg} !important;
        }}
        .stMarkdown, .stChatMessageContent {{
            color: {text_color} !important;
        }}
        div[data-testid="stSidebar"] button {{
            background-color: {button_color} !important;
            color: {button_text_color} !important;
            border-radius: 5px;
        }}
        div[data-testid="stSidebar"] button:hover {{
            background-color: #cc0000 !important;
        }}
        
        .stButton > button {{
            background-color: {button_color} !important;
            color: {button_text_color} !important;
        }}
        .stButton > button:hover {{
            background-color: #cc0000 !important;
        }}
        
        .stMarkdown, .stChatMessageContent, .stTextInput > label, .stSelectbox > label, .stSlider > label {{
            color: {text_color} !important;
        }}
        
        .stTextInput > div > div > input {{
            background-color: {input_background_color} !important;
            color: {input_text_color} !important;
        }}
        .stTextInput > div > div > input::placeholder {{
            color: {input_text_color} !important;
            opacity: 0.7; /* Placeholder rengini biraz daha açık yap */
        }}
    </style>
""", unsafe_allow_html=True)


st.title("Smart Search and Generation Wizard 🧙‍♂️✨")
st.caption("Step into the magical world of knowledge! 🔍✨ The RAG wizard is here to help you find everything you need and generate brilliant ideas.")

# Sidebar (Model and History)
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["qwen2.5:3b", "llama3.2:latest", "phi3:latest", "deepseek-r1:8b"],
        index=0
    )
    st.divider()
    st.markdown("**📌 Model Capabilities**")
    st.write("""
    - Fast and Accurate Information Retrieval 🚀 
    - Smart Text Generation and Summarization 📝 
    - Multi-Source Data Integration 🌐 
    """)
    st.divider()
    st.header("📜 Chat History")
    if st.button("Clear Chat History ❌"):
        clear_chat_history()
    
    # Show last 8 chat history
    history = load_chat_history()
    for msg in history[-8:]:  
        st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")
    st.divider()

# Define LLM Engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# Load chat history
if "message_log" not in st.session_state:
    st.session_state.message_log = load_chat_history()

# Chat container
chat_container = st.container()

with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)

# Message from user sendings
user_query = st.chat_input("Type your question here ...")

# Sending prompt_chain to ai
def generative_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [SystemMessagePromptTemplate.from_template( 
        
        "You are an expert AI assistant. Comment on any programming"
        "language code given to you by the user, correct it and"
        "give him the answer he wants. If necessary, reorganize the code and present it to him."
        "and your primary goal is to provide quick, accurate, and effective answers to users' questions." 
        "You must generate responses in English, but if the user specifically requests a response "
        "in Turkish, you can answer in Turkish."

    )]
    
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    
    return ChatPromptTemplate.from_messages(prompt_sequence)


if user_query:
    # Save message to chat history
    st.session_state.message_log.append({"role": "user", "content": user_query})
    save_chat_history(st.session_state.message_log)

    # Response ai
    with st.spinner("Working my magic... 🧙‍♂️✨"):
        prompt_chain = build_prompt_chain()
        ai_response = generative_ai_response(prompt_chain)

    # Save ai response
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    save_chat_history(st.session_state.message_log)

    # Display AI response in a typed manner
    with chat_container:
        with st.chat_message("ai"):
            response_placeholder = st.empty()
            full_response = ""
            for chunk in ai_response.split():  # write letter-to-letter
                full_response += chunk + " "
                time.sleep(0.01)  # wait 0.01 second
                response_placeholder.markdown(full_response + "▌")  # show letter-to-letter
            response_placeholder.markdown(full_response)  # show completed 

    st.rerun()