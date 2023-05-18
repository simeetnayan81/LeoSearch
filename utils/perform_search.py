
from utils import hf
from utils import pinecone_index
def sem_search(query):
	print(query)
	qemb=hf.embed_query(query)
	#print('d2')
	xc = pinecone_index.query(qemb, top_k=7, include_metadata=True)
	results=[]
	cnt=1
	for result in xc['matches']:
		rank = 'Rank: ' + str(cnt)
		results.append({'title': result['metadata']['question'], 'rank': rank})
		cnt=cnt+1
	return results
