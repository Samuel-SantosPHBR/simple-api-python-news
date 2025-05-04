from models.news import *
from playhouse.shortcuts import model_to_dict
import json

class ListNewsUseCase:
    @staticmethod
    def execute():
        print(1)
        news = News.select()
        print(news)
        return [model_to_dict(item) for item in news]