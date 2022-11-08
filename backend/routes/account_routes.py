from flask import Blueprint 
from controllers.accountController import account_login


account_blueprint = Blueprint('blueprint', __name__)

account_blueprint.route('/login', methods=['POST'])(account_login)
