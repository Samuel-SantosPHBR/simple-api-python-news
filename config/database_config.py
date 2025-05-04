from peewee import *
import os

DATABASE = os.getenv('DATABASE')
USER_DATABASE = os.getenv('USER_DATABASE')
PASSWORD_DATABASE = os.getenv('PASSWORD_DATABASE')
HOST_DATABASE = os.getenv('HOST_DATABASE')
PORT_DATABASE = os.getenv('PORT_DATABASE')

db = MySQLDatabase(DATABASE, user=USER_DATABASE, password=PASSWORD_DATABASE,
                         host=HOST_DATABASE, port=int(PORT_DATABASE))