import os
import chainlit as cl
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from langchain.memory import ConversationSummaryBufferMemory

#  Dossier contenant les fichiers PDF
pdf_folder = "data"
big_doc = []

#  Charger les fichiers PDF
for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        documents = loader.load_and_split(text_splitter=text_splitter)
        big_doc.extend(documents)

print(f"{len(big_doc)} documents chargés pour le RAG")

#  Initialisation du modèle d'embedding
model_name = "sentence-transformers/all-MiniLM-L6-v2"
hf_embeddings = HuggingFaceEmbeddings(model_name=model_name)

#  Création du vectorstore pour la recherche
vectorstore = Chroma.from_documents(big_doc, hf_embeddings)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

#  Définition du template de prompt
template = """Tu es un assistant qui répond aux FAQ de l'Institut de Formation et de Recherche en Informatique (IFRI)
de l'Université d'Abomey Calavi (UAC). Utilise l'historique de conversation pour répondre.
Historique : {chat_history}
Question : {question}
Contexte : {context}
Réponse :"""

prompt = ChatPromptTemplate.from_template(template)

#  Initialisation du modèle LLM Hugging Face
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-2-7b-hf", task="text-generation", temperature=0.5, max_new_tokens=1000)

#  Mémoire de conversation
memory = ConversationSummaryBufferMemory(
    llm=llm,
    memory_key="chat_history",
    input_key="question",
    max_token_limit=100
)

#  Création de la chaîne RAG
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={
        "prompt": prompt,
        "memory": memory
    }
)

#  Fonction de démarrage du chat
@cl.on_chat_start
async def start_chat():
    msg = cl.Message(content="")
    start_message = "Hello, I'm your 100% IFRI 💻📚 Agent 🤖. How can I help you today?"

    for token in start_message:
        await msg.stream_token(token)

    await msg.send()

#  Gestion des messages utilisateurs
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = rag_chain.run(user_input)

    msg = cl.Message(content="")
    for token in str(response):
        await msg.stream_token(token)

    await msg.send()

#  Lancement de l'application
if __name__ == "__main__":
    cl.run("app.py")
