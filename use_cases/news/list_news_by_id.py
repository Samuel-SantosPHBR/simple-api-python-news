from models.news import *
from playhouse.shortcuts import model_to_dict

class ListNewsById:
    @staticmethod
    def execute(id):
        news = News.get(News.id == id)
        print(news)
        return [model_to_dict(news)]