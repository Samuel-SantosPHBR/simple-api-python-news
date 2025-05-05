from models.news import *
from playhouse.shortcuts import model_to_dict

class UpdateNewsUseCase:
    @staticmethod
    def execute(payload,id):
        News.update(title = payload.title, content = payload.content, author = payload.author).where(News.id == id).execute()

        updated_news = News.get(News.id == id)
        return model_to_dict(updated_news)