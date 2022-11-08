from flask import jsonify, request
import database as db_config
from models.record_all import Record, record_schema, records_schema
from public_functions.functions import generate_limits

db = db_config.db_sql

def add_record():
    transaction_id = request.json['transaction_id']
    description = request.json['description']
    transaction_date = request.json['transaction_date']
    record = Record(transaction_id, description, transaction_date)
    db.session.add(record)
    db.session.commit()
    return record_schema.jsonify(record) 

def get_records(): 
    all_records = Record.query.all()
    result = records_schema.dump(all_records)
    return jsonify(result)

def get_records_month(year, month):
    limit1, limit2 = generate_limits(year, month)
    records_filtered = db.session.query(Record).filter(
            Record.transaction_date.between(limit1, limit2))
    result = records_schema.dump(records_filtered)
    return jsonify(result)

