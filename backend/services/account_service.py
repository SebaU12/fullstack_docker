from flask import jsonify, request
import database as db_config
from werkzeug.security import check_password_hash
from os import environ 
from dotenv import load_dotenv, find_dotenv
from jwt import encode
from datetime import datetime, timedelta

load_dotenv(find_dotenv())
db=db_config.dbConnection_mongo()

def expire_token():
    now = datetime.now()
    date_expiration = now + timedelta(1) 
    return date_expiration

def login():
    req_username = request.json['username']
    req_password = request.json['password']
    if req_username and req_password: 
        accounts = db.accounts
        account = accounts.find_one({"username": req_username})
        if account:
            password = req_password + environ.get("SECRET_KEY") 
            if check_password_hash(account['password'], password):
                token = encode(payload={
                    "username": req_username,
                    "email": account["email"],
                    "exp": expire_token()
                    }, key= environ.get("SECRET_KEY_TOKEN"),
                       algorithm="HS256")
                return token.encode("UTF-8") 
            return jsonify({"message":"Incorrect password"})
        return jsonify({"message":"Username does not exist on DB"})

