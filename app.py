from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from db import db
from controllers.books import books


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_namespace(books)


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
