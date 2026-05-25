from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
def embeddings(chunks,embedding_model):

    vectorstore = FAISS(
        chunks,
        embedding_model
    )
    
    return vectorstore