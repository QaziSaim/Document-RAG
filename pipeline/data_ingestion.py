from langchain_community.document_loaders import PyPDFLoader

import os

folder_path = "../documents"
document_path = "pokemonscript.pdf"
def loaded_documents(folder_path,file_path):
    final_path  = os.path.join(folder_path,file_path)
    if os.path.exists(final_path):
        print('PDF Found')
        
        loader = PyPDFLoader(final_path)
        documents = loader.load()
        return documents
    else:
        return "Document Not Found Please Enter Correct Path.."
    # print(documents[0].page_content)
if __name__=="__main__":
    loaded_documents()

