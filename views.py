import time
from flask import request, jsonify
import logging

from config import Cache, cache, mail
from models import generate_otp, send_otp_email

logging.basicConfig(level=logging.DEBUG)

def request_otp():
    data = request.json
    email = data.get('email')

    if email:
        otp = generate_otp()
        cache.set(email, otp)
        retries = 3
        for attempt in range(retries):
            try:
                send_otp_email(email, otp)
                logging.info(f'OTP sent to {email}')
                return jsonify({'message': 'OTP sent successfully'}), 200
            except Exception as e:
                logging.error(f'Failed to send OTP on attempt {attempt + 1}: {e}')
                if attempt < retries - 1:
                    time.sleep(5)  # Wait for 5 seconds before retrying
                else:
                    return jsonify({'error': f'Failed to send OTP after {retries} attempts: {e}'}), 500
    logging.warning('Email is required')
    return jsonify({'error': 'Email is required'}), 400


def verify_otp():
    data = request.json
    email = data.get('email')
    otp = data.get('otp')

    if not email or not otp:
        return jsonify({'error': 'Email and OTP is required'}), 400

    stored_otp = cache.get(email)
    if stored_otp and stored_otp == otp:
        cache.delete(email)
        return jsonify({'message':'OTP verification successful'}), 200
    else:
        return jsonify({'error': 'OTP verification failed'}), 400
