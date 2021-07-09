from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )


    def post(self):
        data = User.parser.parse_args()
        user = UserModel(data['username'], data['password'])
        user.save_to_db()


class UserList(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}





