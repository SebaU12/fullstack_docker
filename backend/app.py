from flask import Flask, jsonify
import database as dbase
from os import environ 
from dotenv import load_dotenv, find_dotenv
from routes.account_routes import account_blueprint
from database import db_sql, ma 
from routes.record_ventas_routes import record_blueprint, record_middleware_blueprint
from routes.record_all_routes import record_all_blueprint, record_all_middleware_blueprint
from routes.purchase_request_routes import purchase_request_blueprint, purchase_request_middleware_blueprint 
from routes.inventory_request_routes import inventory_request_blueprint, inventory_request_middleware_blueprint 
from routes.contabilidad import contabilidad_blueprint 

from flask_cors import CORS

load_dotenv(find_dotenv())
db = dbase.dbConnection_mongo()

app = Flask(__name__)
app.register_blueprint(account_blueprint, url_prefix='/account')
app.register_blueprint(record_blueprint, url_prefix='/record')
app.register_blueprint(record_middleware_blueprint, url_prefix='/record_middleware')
app.register_blueprint(record_all_blueprint, url_prefix='/record_all')
app.register_blueprint(record_all_middleware_blueprint, url_prefix='/record_all_middleware')
app.register_blueprint(purchase_request_blueprint, 
                       url_prefix='/purchase_request')
app.register_blueprint(purchase_request_middleware_blueprint, 
                       url_prefix='/purchase_request_middleware')
app.register_blueprint(inventory_request_blueprint, 
                       url_prefix='/inventory_request')
app.register_blueprint(inventory_request_middleware_blueprint, 
                       url_prefix='/inventory_request_middleware')
app.register_blueprint(contabilidad_blueprint, url_prefix='/contabilidad')

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQL_URI_DB1")
app.config['SQLALCHEMY_BINDS'] = {'two': environ.get("SQL_URI_DB2"), 
                                  'three': environ.get("SQL_URI_DB3")}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db_sql.init_app(app)
ma.init_app(app)

CORS(app)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "API FUNCIONANDO"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=environ.get("PORT_TEST"), debug=True)
