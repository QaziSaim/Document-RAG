from data_ingestion import loaded_documents
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

def text_to_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap = 50
    )
    chunks = splitter.split_documents(documents)
    print(chunks[0].page_content)
    return chunks

if __name__=="__main__":
    folder_path = "../documents"
    document_path = "pokemonscript.pdf"
    text_to_chunks(loaded_documents(folder_path,document_path))
