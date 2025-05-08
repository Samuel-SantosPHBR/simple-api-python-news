from config.database_config import *

class Users(Model):
    id = IntegerField(primary_key=True)
    email = CharField()
    password = CharField()
    name = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        database = db