from flask import Blueprint, request
from controllers.inventory_requestController import create_request, list_request, update_request
from middleware.check_auth import checkAuth

inventory_request_blueprint = Blueprint('blueprint_irequest', __name__)
inventory_request_middleware_blueprint = Blueprint('blueprint_irequest_middleware'
                                                    , __name__)

inventory_request_blueprint.route('/create_request', methods=['POST'])(create_request)

@inventory_request_middleware_blueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    if checkAuth(token, output=False) != True:
        return "No valido"

inventory_request_middleware_blueprint.route('/get_all', methods=['GET'])(list_request)
inventory_request_middleware_blueprint.route('/confirm/<id>', methods=['PUT'])(update_request)
