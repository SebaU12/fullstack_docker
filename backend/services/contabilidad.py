from flask import jsonify, request
import database as db_config
#from models.Tactivo import Tactivo, tactivo_schema, tactivos_schema 
from models.record_all import Record, record_schema, records_schema
from models.record_ventas import RecordVentas, record_schema, records_schema
from middleware.check_auth import getEmail  
from public_functions.functions import generate_limits, sum_values_json 

from controllers.record_ventasController import list_records_month as list_ventas 
from controllers.record_allController import list_records_month as list_compras

db = db_config.db_sql

def generate_Tactivo(year, month):
    records_ventas = list_ventas(year, month)
    records_compras = list_compras(year, month)
    valor_total_ventas = sum_values_json(records_ventas, "value") 
    valor_total_compras = sum_values_json(records_compras, "value") 
    resultado = valor_total_ventas - valor_total_compras 
    result_json = {
            "debito" : records_ventas.get_json(), 
            "credito" : records_compras.get_json(), 
            "resultado": resultado 
        }
    return result_json  

def generate_Tpasivo(year, month): 
    records_ventas = list_ventas(year, month)
    pago_banco = 200 
    salarios = 200 
    impuesto = 0.1 
    credito = 400 
    valor_impuesto = sum_values_json(records_ventas, "value") * impuesto 
    resultado = pago_banco+salarios+valor_impuesto-credito
    result_json = {
            "debito" : {
                "banco": pago_banco, 
                "salarios":salarios, 
                "ganancia": valor_impuesto
                }, 
            "credito" : credito, 
            "resultado" : resultado 
            }
    return result_json 

def generate_Tcapital(year, month): 
    activo = generate_Tactivo(year, month) 
    pasivo = generate_Tpasivo(year, month) 
    activo_debito = activo["debito"]
    activo_credito = activo["credito"]
    pasivo_credito = pasivo["credito"]
    print(pasivo_credito)
    debito_activo_total = sum_values_json(activo_debito, "value", False)
    credito_activo_total = sum_values_json(activo_credito, "value", False)
    resultado = debito_activo_total - credito_activo_total - float(pasivo_credito)  
    result_json = {
            "debito" : {
                "activo" : activo_debito
                },
            "credito" : {
                "activo" : activo_credito,  
                "pasivo" : pasivo_credito
                },
            "resultado" : resultado
            }
    return result_json 

def generate_Tpatrimonio(year, month): 
    records_ventas = list_ventas(year, month)
    records_compras = list_compras(year, month)
    valor_total_ventas = sum_values_json(records_ventas, "value") 
    valor_total_compras = sum_values_json(records_compras, "value") 
    resultado = valor_total_compras  - valor_total_ventas 
    result_json = {
            "credito" : records_ventas.get_json(), 
            "debito" : records_compras.get_json(), 
            "resultado": resultado 
        }
    return result_json  
