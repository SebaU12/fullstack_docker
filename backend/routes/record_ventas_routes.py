from flask import Blueprint, request
from controllers.record_ventasController import get_file_ventas, post_record, list_records, get_records_month, get_file_ventas 
from middleware.check_auth import checkAuth

record_blueprint = Blueprint('blueprint_ventas', __name__)
record_middleware_blueprint = Blueprint('blueprint_ventas_middleware', __name__)

@record_middleware_blueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    if checkAuth(token, output=False) != True:
        return "No valido"

record_blueprint.route('/post_ventas', methods=['POST'])(post_record)
record_middleware_blueprint.route('/get_all', methods=['GET'])(list_records)
record_middleware_blueprint.route('/get_month/<year>/<month>', 
        methods=['GET'])(get_records_month)
record_blueprint.route('/get_file/<file_id>', 
        methods=['GET'])(get_file_ventas)
