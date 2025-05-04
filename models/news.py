from config.database_config import *

class News(Model):
    id = IntegerField(primary_key=True)
    title = CharField()
    content = TextField()
    author = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        database = db