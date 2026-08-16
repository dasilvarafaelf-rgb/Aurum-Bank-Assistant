import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()

#Funções

@st.cache_resource
def load_llm():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
llm = load_llm()
@st.cache_resource 
def load_vectorstore():
    embed_model = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")
    if os.path.exists(VECTORSTORE_DIR):
        vectorstore = FAISS.load_local(
            VECTORSTORE_DIR,
            embed_model,
            allow_dangerous_deserialization=True,
        )
        return vectorstore
    else:
        raise FileNotFoundError("VectorStore não encontrado, rode 'ingest.py' primeiro.")

VECTORSTORE_DIR = "vectorstore"
vectorstore = load_vectorstore()

# HISTÓRICO

historicos = {}


def responder(pergunta: str, session_id: str = "default") -> str:
    """Realiza a busca na base vetorial e gera a resposta."""

    historico = historicos.setdefault(session_id, [])

    documentos = vectorstore.similarity_search(
        pergunta,
        k=4,
    )

    if not documentos:
        return "Não encontrei essa informação na documentação da empresa."

    contexto = "\n\n".join(
        doc.page_content for doc in documentos
    )

    conversa = "\n".join(historico[-8:])

    prompt = f"""
Você é o assistente virtual da empresa Banco Aurum Digital

Sua função é responder dúvidas dos colaboradores utilizando EXCLUSIVAMENTE
as informações presentes na documentação interna da empresa.

=========================
REGRAS
=========================

1. Utilize apenas as informações do contexto recuperado.

2. Nunca invente informações ou complemente respostas com conhecimento próprio.

3. Explique o conteúdo com suas próprias palavras, evitando copiar grandes trechos da documentação.

4. Utilize linguagem profissional, clara, objetiva e cordial.

5. Sempre que fizer sentido, organize a resposta em pequenos parágrafos ou listas.

6. Quando a resposta estiver baseada em uma política, manual, procedimento ou diretriz interna, introduza naturalmente com expressões como:
- "Conforme a política da empresa..."
- "Com base na política interna..."
- "Segundo as diretrizes da empresa..."
- "De acordo com o procedimento interno..."

Escolha a expressão que melhor se encaixar na situação.

7. Nunca mencione nomes de arquivos, extensões (.pdf, .docx, .xlsx, .md, .html) ou detalhes técnicos da implementação.

8. Caso a informação não exista na documentação, responda exatamente:
"Não encontrei essa informação na documentação da empresa."

9. Caso a pergunta não esteja relacionada à documentação interna da empresa, responda:
"Posso ajudar apenas com informações presentes na documentação interna do Banco Aurum Digital."

10. Cumprimente, agradeça ou despeça-se naturalmente quando apropriado.

=========================
HISTÓRICO
=========================

{conversa}

=========================
DOCUMENTAÇÃO
=========================

{contexto}

=========================
PERGUNTA
=========================

{pergunta}

=========================
INSTRUÇÃO FINAL
=========================

Escreva uma resposta natural, profissional e objetiva.
Não mencione arquivos ou detalhes técnicos.
Quando apropriado, indique que a resposta está baseada em uma política, procedimento ou diretriz interna da empresa.

Resposta:
"""

    try:
        resposta = llm.invoke(prompt).content.strip()
    except Exception as erro:
        print(f"Erro ao chamar o LLM: {erro}")
        return "Desculpe, mas ocorreu um erro."

    historico.append(f"Usuário: {pergunta}")
    historico.append(f"Assistente: {resposta}")

    if len(historico) > 20:
        del historico[:-20]

    return resposta