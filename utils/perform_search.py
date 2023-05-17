pinecone.init(api_key=PINECONE_KEY, environment="asia-southeast1-gcp-free")
pinecone_index = pinecone.Index("leo-search")
from utils.key import PINECONE_KEY
from utils import hf

def sem_search(query):
	qemb=hf.embed_query(query)
	xc = pinecone_index.query(qemb, top_k=5, include_metadata=True)
	results=[]
	for result in xc['matches']:
		results.append({'title': result['metadata']['question'], 'url':'google.com'})
	return results
	# print(PINECONE_KEY)
	# results = [
    #     {'title': 'Result 1', 'url': 'http://example.com/result1'},
    #     {'title': 'Result 2', 'url': 'http://example.com/result2'},
    #     {'title': 'Result 3', 'url': 'http://example.com/result3'}]
	# return results