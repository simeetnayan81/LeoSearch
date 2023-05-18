# LeoSearch
### A semantic search engine

Leo search is a semantic search engine with following features:
* It uses the top 10K questions from __chenghao/quora_questions__ dataset.
* It uses __sentence-transformers/all-mpnet-base-v2__ to generate the 768 dimensional embedding from each document/question/query.
* Pinecone is used to store and index the embeddings and the questions.
* It uses euclidean distance to find the top 7 nearest questions.

## Running the app locally
1. Clone the repo
2. Install the requirements using `pip install requirements`
3. Export the flask app name using `export FLASK_APP=main.py`
4. Run the app using `flask run`

## Some screenshots
![image](https://github.com/simeetnayan81/LeoSearch/assets/78461155/9f8f3bbe-d461-4d65-b972-16e1db34e844)
![image](https://github.com/simeetnayan81/LeoSearch/assets/78461155/3e130fd0-bcf9-4229-b8a0-f8d63e02189e)

