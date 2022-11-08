from pymongo import MongoClient
from os import environ 
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

load_dotenv(find_dotenv())

def dbConnection_mongo():
    try: 
        client = MongoClient(environ.get("MONGO_URI"))
        db = client[environ.get("MONGO_COLLECTION")]
    except ConnectionError:
        print("Error al conectarse a la BD")
    return db 

db_sql = SQLAlchemy()
ma = Marshmallow() 
