from flask import jsonify
from jwt import decode, exceptions
from os import environ 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def checkAuth(token, output=False): 
    try: 
        key_token =  environ.get("SECRET_KEY_TOKEN")
        if output:
            return decode(token, key= key_token,algorithms=["HS256"])
        decode(token, key= key_token ,algorithms=["HS256"])
        return True
    except exceptions.DecodeError:
        res = jsonify({"message": "Invalid token"})
        res.status_code = 401
        return res 
    except exceptions.ExpiredSignatureError:
        res = jsonify({"message": "Token expired"})
        res.status_code = 401
        return res 

def getEmail(token): 
    key_token =  environ.get("SECRET_KEY_TOKEN")
    data = decode(token, key= key_token,algorithms=["HS256"])
    return data["email"]
