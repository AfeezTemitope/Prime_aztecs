from flask_caching import Cache
from flask_mail import Mail

cache = Cache()
mail = Mail()


class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tbelzbby@gmail.com'
    MAIL_PASSWORD = 'coar jkox grbd xomk'
    MAIL_DEFAULT_SENDER = 'tbelzbby@gmail.com'

    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300
