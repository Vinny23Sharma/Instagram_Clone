import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.user import User, UserList

app = Flask(__name__)
CORS(app)


uri = os.getenv('DATABASE_URL')
if uri and uri.startswith('postgres://'):
    uri = uri.replace('postgres://','postgresql://',1)
else:
    uri = 'sqlite:///data.db'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)



api.add_resource(User,"/user")
api.add_resource(UserList,"/users")


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
