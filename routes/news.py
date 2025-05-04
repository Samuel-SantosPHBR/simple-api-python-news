from config.api_config import app
from use_cases.news import create_news_use_case, list_news_use_case
from pydantic import BaseModel


class NewsRequestDto(BaseModel):
    title: str
    content: str
    author: str

@app.post("/news")
async def root(payload: NewsRequestDto):
    create_news_use_case.CreateNewsUseCase.execute(payload)

@app.get("/news")
async def root():
    return list_news_use_case.ListNewsUseCase.execute()

@app.get("/news/{id}")
async def root(id):
    return {"message": id}

@app.patch("/news/{id}")
async def root():
    return {"message": "Hello World"}