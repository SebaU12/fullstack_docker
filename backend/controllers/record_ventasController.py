import database as db_config
from services.record_ventas_service import add_record, get_records, get_records_month 

db=db_config.db_sql

def post_record():
    return add_record()

def list_records():
    return get_records()

def list_records_month(year, month):
    if(int(month) < 1 or int(month) > 12):
        return "Mes invalido"
    else: 
        return get_records_month(int(year), int(month))
