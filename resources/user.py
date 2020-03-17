
from flask_restful import Resource, reqparse
from models.Users import UserModel

class UserReister(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="Username is required")
    parser.add_argument('password',type=str,required=True,help="password is required")

    def post(self):

        data=UserReister.parser.parse_args()
        if UserModel.by_username(data['username']):
            return ({"message":"user already exist"},400)

        user=UserModel(**data)
        user.save_to_db()
        return {"message":"User created"},201
