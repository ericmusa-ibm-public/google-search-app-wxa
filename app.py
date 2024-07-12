from fastapi import FastAPI
from googlesearch import search
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def hello_world():
    return {"message": 'Hello, World!'}


class Query(BaseModel):
    query: str


class SearchResponse(BaseModel):
    results: list[str]


@app.post('/search')
def web_search(query: Query):
    results = search(query.query, num_results=10)
    return SearchResponse(results=list(res for res in results))

