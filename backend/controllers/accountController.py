import database as db_config
from services.account_service import login

db=db_config.dbConnection_mongo()

def account_login():
    return login()
