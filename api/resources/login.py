from flask_restful import Resource, reqparse
from api.common.util import ResponseUtil


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, help="Username cannot be blank!")
        parser.add_argument('password', required=True, help="Password cannot be blank!")
        args = parser.parse_args()
        username = args.get('username', None)
        password = args.get('password', None)

        if not username or not password:
            return ResponseUtil.send_custom_failure('Username and Password are required.', 400)

        data = {
            'username': username,
            'password': password
        }
        return ResponseUtil.send_ok(data)
