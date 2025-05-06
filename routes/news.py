from config.api_config import app
from use_cases.news import create_news_use_case, list_news_use_case, list_news_by_id, update_news_use_case, delete_news_use_case
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
    return list_news_by_id.ListNewsById.execute(id)

@app.patch("/news/{id}")
async def root(payload: NewsRequestDto, id):
    update_news_use_case.UpdateNewsUseCase.execute(payload, id)

@app.delete("/news/{id}")
async def root(id):
    delete_news_use_case.DeleteNewsUseCase.execute(id)