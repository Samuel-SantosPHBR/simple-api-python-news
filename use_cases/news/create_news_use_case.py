from models.news import *

class CreateNewsUseCase:
    @staticmethod
    def execute(payload):
        News.create(title = payload.title, content = payload.content, author = payload.author)