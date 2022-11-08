from flask import jsonify, request
import database as db_config
from models.purchase_request import PRequest, prequest_schema, prequests_schema
from middleware.check_auth import getEmail  

db = db_config.db_sql

def send_request():
    amount = request.json['amount']
    supplier = request.json['supplier']
    request_date = request.json['request_date']
    motive = request.json['motive']
    purchase_request = PRequest(amount, supplier, 
            request_date, motive)
    db.session.add(purchase_request)
    db.session.commit()
    return prequest_schema.jsonify(purchase_request) 

def get_requests(): 
    all_request = db.session.query(PRequest).filter(
            PRequest.state==False)
    result = prequests_schema.dump(all_request)
    return jsonify(result)

def update_state(id):
    prequest = PRequest.query.get(id)
    email = getEmail(token = request.headers['Authorization'].split(" ")[1])
    prequest.state = True
    prequest.email_check = email
    db.session.commit()
    return prequest_schema.jsonify(prequest)

