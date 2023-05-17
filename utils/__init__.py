import pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings


model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)

from utils import perform_search