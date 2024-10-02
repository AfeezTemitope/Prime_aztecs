import random
from flask_mail import Message

from config import mail


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(email, otp):
    message = Message('Your OTP has been sent', recipients=[email])
    message.body = f'Your OTP is {otp}'
    return mail.send(message)
