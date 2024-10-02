from flask import Flask
from flask_mail import Mail
from flask_caching import Cache
from urls import pa
from config import Config, cache, mail

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(pa)
mail.init_app(app)
cache.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
