from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()



openai_embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = FAISS.load_local(
    "vectors",
    openai_embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type='similarity',
    search_kwargs={'k':3}
)

llm = ChatOpenAI(model='gpt-4o-mini')


system_prompt = (
    "You are an pokemon fan with hudge knowledge of pokemon any question ask you can answer and you also have knowledge of pokemon unrleased moive team rocket vs team plasama.\n"
    "Any Question which you know answer from script if you don't know say i don't know.\n\n"
    "{context}"
)
prompt = ChatPromptTemplate.from_messages([
    ("system",system_prompt),
    ("human","{input}")
])

parser = StrOutputParser()
question_answer_chain = create_stuff_documents_chain(llm,prompt) | parser
rag_chain = create_retrieval_chain(retriever,question_answer_chain)

# response = rag_chain.invoke({'input':'who is the main villan in movie'})

# print(response['answer'])

def ask_question(query):
    response = rag_chain.invoke({'input':query})
    return response['answer']


if __name__=="__main__":
    user_input = input("Enter Your Query:")
    ask_question(user_input)

