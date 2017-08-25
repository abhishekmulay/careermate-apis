class ResponseUtil(object):
    @staticmethod
    def send_ok(data):
        return ResponseUtil._send_response('ok', 200, data)

    @staticmethod
    def send_bad_params():
        return ResponseUtil._send_response('Bad or missing valid parameters', 400)

    @staticmethod
    def send_not_found():
        return ResponseUtil._send_response('Resource not found', 404)

    @staticmethod
    def send_custom_failure(message, code=400):
        return ResponseUtil._send_response(message, code)

    @staticmethod
    def _send_response(message, code, data=None):
        if data:
            return {'data': {'data': data, 'message': message, 'status_code': code}}, code, {'Content-Type': 'application/json'}
        else:
            return {'data': {'message': message, 'status_code': code}}, code, {'Content-Type': 'application/json'}