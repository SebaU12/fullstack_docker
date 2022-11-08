from flask import Blueprint, request
from controllers.purchase_requestController import create_request, list_request, update_request
from middleware.check_auth import checkAuth

purchase_request_blueprint = Blueprint('blueprint_prequest', __name__)
purchase_request_middleware_blueprint = Blueprint('blueprint_prequest_middleware'
                                                    , __name__)
@purchase_request_middleware_blueprint.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    if checkAuth(token, output=False) != True:
        return "No valido"

purchase_request_blueprint.route('/create_request', methods=['POST'])(create_request)
purchase_request_middleware_blueprint.route('/get_all', methods=['GET'])(list_request)
purchase_request_middleware_blueprint.route('/confirm/<id>', methods=['PUT'])(update_request)
