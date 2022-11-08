from flask import jsonify, request
import database as db_config
from models.inventory_request import IRequest, irequest_schema, irequests_schema 
from middleware.check_auth import getEmail  

db = db_config.db_sql

def send_request():
    product_id = request.json['product_id']
    request_date = request.json['request_date']
    motive = request.json['motive']
    value = request.json['value']
    irequest = IRequest(product_id, request_date, motive, value)
    db.session.add(irequest)
    db.session.commit()
    return irequest_schema.jsonify(irequest) 

def get_requests(): 
    all_request = db.session.query(IRequest).filter(
            IRequest.state==False)
    result = irequests_schema.dump(all_request)
    return jsonify(result)

def update_state(id):
    irequest = IRequest.query.get(id)
    email = getEmail(token = request.headers['Authorization'].split(" ")[1])
    irequest.state = True
    irequest.email_check = email
    db.session.commit()
    #return irequest_schema.jsonify(irequest)
    return email 

