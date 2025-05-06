from models.news import *
from playhouse.shortcuts import model_to_dict

class DeleteNewsUseCase:
    @staticmethod
    def execute(id):
        News.delete().where(News.id == id).execute()
        return ("Notícia: {id} deletada!")