from dotenv import load_dotenv
load_dotenv()
from config.database_config import db
from models.news import *
from routes.news import *
from models.users import *
from routes.users import *

db.create_tables([News])
db.create_tables([Users])

# importando as rotas