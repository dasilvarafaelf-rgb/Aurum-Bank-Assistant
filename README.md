# 🏦 Aurum Bank Assistant

O **Aurum Bank Assistant** é um assistente virtual desenvolvido para auxiliar funcionários de um banco digital, respondendo dúvidas de forma rápida e contextualizada a partir de uma base de conhecimento própria.

## 🚀 Demonstração

**Acesse o aplicativo:**
[🔗 Aurum Bank Assistant](COLE_AQUI_O_LINK_DO_STREAMLIT)

## 💡 Sobre o aplicativo

O Aurum Bank Assistant funciona como um atendente virtual capaz de interpretar perguntas dos usuários e consultar uma base de conhecimento antes de gerar uma resposta.

A aplicação utiliza **RAG (Retrieval-Augmented Generation)** para combinar a recuperação de informações relevantes com um modelo de linguagem, permitindo que as respostas sejam baseadas nos conteúdos disponíveis sobre o banco.

### ✨ Principais funcionalidades

* 💬 Conversação em linguagem natural
* 🔎 Busca semântica na base de conhecimento
* 🤖 Geração de respostas utilizando Llama 3.3
* 🏦 Respostas baseadas nos documentos do Aurum Bank
* ⚡ Interface interativa desenvolvida com Streamlit

## 🧠 Fluxo da aplicação

O funcionamento do Aurum Bank Assistant pode ser dividido em duas etapas principais: **construção da base de conhecimento** e **processamento das perguntas do usuário**.

### 1. 📚 Construção da base de conhecimento

Antes das perguntas chegarem ao assistente, os documentos disponibilizados pelo banco são processados pelo `ingest.py`.

O fluxo acontece da seguinte maneira:

```text
Documentos do banco
        ↓
Leitura dos arquivos
        ↓
Divisão dos documentos em trechos
        ↓
Geração dos embeddings
        ↓
Armazenamento no FAISS
        ↓
VectorStore
```

Os documentos são transformados em pequenos trechos para facilitar a recuperação das informações. Cada trecho recebe uma representação vetorial (*embedding*), permitindo que o sistema encontre conteúdos semanticamente relacionados a uma pergunta.

Esses vetores são armazenados no **FAISS**, formando o `vectorstore` utilizado pelo assistente.

### 2. 💬 Processamento da pergunta

Quando o usuário envia uma pergunta pelo Streamlit, ela passa pelo fluxo principal do `agente_aurum.py`.

```text
Usuário
   ↓
Interface Streamlit
   ↓
Pergunta enviada ao agente
   ↓
Busca no VectorStore
   ↓
Trechos relevantes recuperados
   ↓
Contexto + pergunta
   ↓
Llama 3.3 via Groq
   ↓
Resposta gerada
   ↓
Exibição no Streamlit
```

Primeiramente, a pergunta é recebida pelo aplicativo e encaminhada para o agente.

O agente utiliza o **VectorStore** para realizar uma busca semântica e recuperar os trechos da base de conhecimento que possuem maior relação com a pergunta.

Esses conteúdos recuperados são então utilizados como **contexto** para o modelo de linguagem.

A pergunta do usuário e o contexto encontrado são enviados ao **Llama 3.3**, executado através da API da **Groq**. O modelo utiliza essas informações para elaborar a resposta final.

Por fim, a resposta retorna para o Streamlit e é apresentada ao usuário na interface de conversa.

### 🔄 Resumindo o fluxo

```text
┌──────────────────────┐
│       Usuário        │
│   envia uma pergunta │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│      Streamlit       │
│ recebe a pergunta   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│     Aurum Agent      │
│  processa a consulta │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│      VectorStore      │
│ busca contexto        │
│     relevante         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│      Llama 3.3        │
│ recebe pergunta +    │
│      contexto         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       Resposta        │
│  exibida ao usuário   │
└──────────────────────┘
```

Dessa forma, o modelo não depende apenas do conhecimento geral que possui. Ele recebe informações recuperadas especificamente da base do Aurum Bank, tornando o processo mais direcionado ao contexto da aplicação.

## 🛠️ Tecnologias

* **Python** — desenvolvimento da aplicação
* **Streamlit** — interface web
* **LangChain** — integração e gerenciamento do fluxo de IA
* **Groq** — execução do modelo de linguagem
* **Llama 3.3** — modelo utilizado para geração das respostas
* **Hugging Face** — geração dos embeddings
* **FAISS** — armazenamento e busca vetorial

## 📂 Estrutura do projeto

```text
Aurum-Bank-Assistant/
├── files/                  # Base de documentos do banco
├── vectorstore/            # Base vetorial
├── agente_aurum.py        # Lógica do assistente
├── ingest.py              # Processamento dos documentos
├── #Streamlit.py          # Interface da aplicação
├── requirements.txt       # Dependências
└── .gitignore
```

## 🎯 Objetivo

O projeto foi desenvolvido como uma aplicação prática de **Inteligência Artificial Generativa**, explorando RAG, embeddings, busca vetorial e integração com modelos de linguagem.

A proposta é demonstrar como essas tecnologias podem ser combinadas para criar um assistente especializado, capaz de consultar uma base de conhecimento específica e transformar as informações encontradas em respostas naturais para o usuário.

## 👨‍💻 Autor

**Rafael da Silva**

[GitHub](https://github.com/dasilvarafaelf-rgb)

