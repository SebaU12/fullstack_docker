from flask import Blueprint, request
from controllers.record_allController import post_record, list_records, list_records_month 
from middleware.check_auth import checkAuth

record_all_blueprint = Blueprint('blueprint_record', __name__)
record_all_middleware_blueprint = Blueprint('blueprint_recorda_middleware'
                                                    , __name__)
@record_all_middleware_blueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    if checkAuth(token, output=False) != True:
        return "No valido"

record_all_blueprint.route('/post_record', methods=['POST'])(post_record)
record_all_middleware_blueprint.route('/get_all', methods=['GET'])(list_records)
record_all_middleware_blueprint.route('/get_month/<year>/<month>', 
        methods=['GET'])(list_records_month)
