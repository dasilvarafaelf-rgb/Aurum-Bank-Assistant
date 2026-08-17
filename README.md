# 🏦 Aurum Bank Assistant

Assistente virtual desenvolvido para auxiliar clientes do **Aurum Bank** com informações e dúvidas relacionadas aos serviços bancários.

## 🚀 Demonstração

**Acesse o aplicativo:**
[🔗 Aurum Bank Assistant](COLE_AQUI_O_LINK_DO_STREAMLIT)

<!-- Depois de enviar seu print para o GitHub, você pode colocar a imagem aqui:
![Aurum Bank Assistant](screenshot.png)
-->

## 💡 Sobre o projeto

O Aurum Bank Assistant utiliza **Inteligência Artificial** para responder perguntas relacionadas ao banco a partir de uma base de documentos.

O projeto utiliza uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)**, permitindo que o modelo consulte informações relevantes antes de gerar uma resposta.

## 🛠️ Tecnologias utilizadas

* Python
* Streamlit
* LangChain
* Groq
* Llama 3.3
* Hugging Face
* FAISS
* Python-dotenv

## 📂 Estrutura do projeto

```text
Aurum-Bank-Assistant/
├── files/                  # Documentos utilizados pelo assistente
├── vectorstore/            # Base vetorial gerada a partir dos documentos
├── agente_aurum.py        # Lógica principal do assistente
├── ingest.py              # Criação da base vetorial
├── #Streamlit.py          # Aplicação Streamlit
├── requirements.txt       # Dependências do projeto
└── .gitignore             # Arquivos ignorados pelo Git
```

## ⚙️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/dasilvarafaelf-rgb/Aurum-Bank-Assistant.git
cd Aurum-Bank-Assistant
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a chave da Groq

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

### 4. Gere o VectorStore

```bash
python ingest.py
```

### 5. Execute o aplicativo

```bash
streamlit run "#Streamlit.py"
```

## 🔐 Variáveis de ambiente

O projeto utiliza:

```text
GROQ_API_KEY
```

**Não compartilhe sua chave de API nem envie o arquivo `.env` para o GitHub.**

No Streamlit Cloud, a chave deve ser configurada através dos **Secrets** da aplicação.

## 📌 Observações

O `vectorstore/` precisa estar disponível para que o assistente consiga consultar a base de conhecimento.

Caso os documentos da pasta `files/` sejam alterados, execute novamente:

```bash
python ingest.py
```

para atualizar a base vetorial.

## 👨‍💻 Autor

**Rafael da Silva**

[GitHub](https://github.com/dasilvarafaelf-rgb)
