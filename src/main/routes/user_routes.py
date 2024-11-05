from flask import Blueprint, jsonify

from src.erros.error_handler import handle_errors
from src.main.composer.user_list_composer import user_list_composer
from src.views.http_types.http_request import HttpRequest

user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route("/userList", methods=["GET"])
def list_users():
    # quando for post ou put
    # http_request = HttpRequest(body=request.json)
    try:
        http_request = HttpRequest()
        view = user_list_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
