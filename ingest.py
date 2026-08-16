import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

PASTA_DOCUMENTOS = r"C:\Users\Lenovo\Desktop\python\Tech Ai project\files"
VECTORSTORE_DIR = "vectorstore"

# Dicionário: extensão -> loader correspondente
LOADERS = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
}

def carregar_todos_os_documentos():
    todas_paginas = []

    for nome_arquivo in os.listdir(PASTA_DOCUMENTOS):
        caminho = os.path.join(PASTA_DOCUMENTOS, nome_arquivo)
        extensao = os.path.splitext(nome_arquivo)[1].lower()

        loader_class = LOADERS.get(extensao)
        if loader_class is None:
            print(f"Tipo não suportado, pulando: {nome_arquivo}")
            continue

        loader = loader_class(caminho)
        paginas = loader.load()

        # Metadado simples indicando de qual arquivo veio (útil para debug)
        for pagina in paginas:
            pagina.metadata["origem"] = nome_arquivo

        todas_paginas.extend(paginas)
        print(f"Carregado: {nome_arquivo} ({len(paginas)} páginas)")

    return todas_paginas


if __name__ == "__main__":
    paginas = carregar_todos_os_documentos()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(paginas)

    embed_model = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")
    vectorstore = FAISS.from_documents(chunks, embed_model)
    vectorstore.save_local(VECTORSTORE_DIR)

    print(f"Vectorstore criado com {len(chunks)} chunks, salvo em '{VECTORSTORE_DIR}'.")