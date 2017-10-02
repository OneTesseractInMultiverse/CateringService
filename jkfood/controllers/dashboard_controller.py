from jkfood import app
from flask import jsonify, request, render_template


# --------------------------------------------------------------------------
# GET: /
# --------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def get_dashboard_root():
    """
        Gets the requester's IP Address and the User Agent and builds a tiny
        service status response message
        :return: Status response json
    """
    return render_template("dashboard/index.html")


# --------------------------------------------------------------------------
# GET: /servicios
# --------------------------------------------------------------------------
@app.route('/services', methods=['GET'])
def get_services():
    """
        Displays a given page
    """
    return render_template("dashboard/services.html")


