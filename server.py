from dotenv import load_dotenv
load_dotenv()
from config.database_config import db
from models.news import *
from routes.news import *

db.create_tables([News])

# importando as rotas