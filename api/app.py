from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS

from resources.login import Login
from resources.signup import Signup

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
CORS(app)

# please keep routes in alphabetical order

api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Signup, '/signup', endpoint='signup')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
