from flask import Blueprint, request
from services.contabilidad import generate_Tactivo, generate_Tpasivo, generate_Tcapital, generate_Tpatrimonio 
from middleware.check_auth import checkAuth

contabilidad_blueprint = Blueprint('blueprint_contabilidad', __name__)
inventory_request_middleware_blueprint = Blueprint('blueprint_irequest_middleware'
                                                    , __name__)


contabilidad_blueprint.route('/generate_Tactivo/<year>/<month>', methods=['GET'])(generate_Tactivo)
contabilidad_blueprint.route('/generate_Tpasivo/<year>/<month>', methods=['GET'])(generate_Tpasivo)
contabilidad_blueprint.route('/generate_Tcapital/<year>/<month>', methods=['GET'])(generate_Tcapital)
contabilidad_blueprint.route('/generate_Tpatrimonio/<year>/<month>', methods=['GET'])(generate_Tpatrimonio)
