import streamlit as st
import uuid
from agente_aurum import responder

st.set_page_config(page_title="Aurum • Assistente Virtual", page_icon="🏛️", layout="wide")

st.markdown("""
<style>
    h1 { color: #d4af37 !important; text-align: center;}
    .stApp {
    background-color: #0e0e10;
}

[data-testid="stChatMessage"]  {
    border-radius:    
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🏛️ Aurum")
    if st.button("Limpar Conversa"):  
        st.session_state.messages = []
        st.rerun()

st.title("Aurum assistente Virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
   st.session_state.session_id = str(uuid.uuid4())

if not st.session_state.messages:
    st.chat_message("assistant", avatar="🏛️").write("Olá! Como posso ajudar?")

# 1. Mostra o histórico já existente (isso e só isso fica no loop)
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🏛️"):
        st.markdown(message["content"])

# 2. Campo de pergunta fixo embaixo, como no Claude
pergunta = st.chat_input("Do your question")

# 3. Só processa quando o usuário manda algo novo (fora do loop)
if pergunta:
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant", avatar="🏛️"):
        with st.spinner("Pensando..."):
            resposta = responder(pergunta, session_id=st.session_state.session_id)
        st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})


