from flask import jsonify, request
import database as db_config
import requests
import json
from models.record_ventas import RecordVentas, record_schema, records_schema
from public_functions.functions import generate_limits

db = db_config.db_sql

def add_record():
    transaction_id = request.json['transaction_id']
    description = request.json['description']
    transaction_date = request.json['transaction_date']
    value = request.json['value']
    record = RecordVentas(transaction_id, description, value, transaction_date)
    db.session.add(record)
    db.session.commit()
    return record_schema.jsonify(record) 

def get_records(): 
    all_records = RecordVentas.query.all()
    result = records_schema.dump(all_records)
    return jsonify(result)

def get_records_month(year, month):
    limit1, limit2 = generate_limits(int(year), int(month))
    records_filtered = db.session.query(RecordVentas).filter(
            RecordVentas.transaction_date.between(limit1, limit2))
    result = records_schema.dump(records_filtered)
    return jsonify(result)

def get_file(file_id): 
    find_record = db.session.query(RecordVentas).filter_by(id = file_id).first()
    if find_record is None: 
        return "No hay archivo"
    else:
        try: 
            flag = False
            url = "http://localhost:3001/ventas"
            r = requests.get(url).json()
            data = json.dumps(r)
            x = json.loads(data)
            for i in range (len(x)):
                if(x[i]["transation_id"] == find_record["transaction_id"]):
                    flag = True
                    return json.dumps(x[i]) 
            if(flag == False):
                return ("No se encontro el archivo")
        except: 
            return "No se pudo generar conexión con la API"

