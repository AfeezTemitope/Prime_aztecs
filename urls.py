from flask import Blueprint
from views import verify_otp, request_otp
pa = Blueprint('prime_aztecs_v1', __name__)


@pa.route('/otp/request', methods=['POST'])
def otp_request_route():
    return request_otp()


@pa.route('/otp/verify', methods=['POST'])
def otp_verify_route():
    return verify_otp()
