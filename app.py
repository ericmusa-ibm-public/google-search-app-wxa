from fastapi import FastAPI
from googlesearch import search
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def hello_world():
    return {"message": 'Hello, World!'}


class Query(BaseModel):
    """
    Using pydantic `BaseModel` with type parameters lets FastAPI know what types are expected in a request
    """
    query: str


class SearchResponse(BaseModel):
    """
    Using pydantic `BaseModel` with type parameters lets FastAPI know what types are to be expected from a response
    """
    results: list[str]


@app.post('/search')
def web_search(query: Query) -> SearchResponse:
    results = search(query.query, num_results=10)
    return SearchResponse(results=list(res for res in results))

