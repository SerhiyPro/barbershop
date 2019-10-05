from server import api, jwt
from flask_restful import Resource, reqparse
from server.models import User
from server.models import RevokedTokenModel
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, \
    jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

parser = reqparse.RequestParser()  # Making those fields required
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if User.get_by_username(data['username']):
            return {'message': f'User {data["username"]} already exists'}, 400

        new_user = User(
            username=data['username'],
            password_hash=User.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])  # to access protected routes
            refresh_token = create_refresh_token(identity=data['username'])  # to reissue access token after expiration
            return {
                       'message': f'User {data["username"]} was successfully created',
                        'access_token': access_token,
                        'refresh_token': refresh_token
                   }, 201
        except:
            return {'message': 'User wasn\'t created, something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()

        current_user = User.get_by_username(data['username'])
        if not current_user:
            return {'message': f'User {data["username"]} doesn\'t exist'}, 400

        if User.verify_hash(data['password'], current_user.password_hash):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                       'message': f'Logged in as {current_user.username}',
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200
        else:
            return {'message': 'Wrong credentials'}, 400


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}, 200
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}, 200
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}, 200


class AllUsers(Resource):
    """Only for testing"""
    @jwt_required
    def get(self):
        return User.return_all(), 200


class SecretResource(Resource):
    """To access only with token"""
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }


api.add_resource(UserRegistration, '/api/registration')
api.add_resource(UserLogin, '/api/login')
api.add_resource(UserLogoutAccess, '/api/logout/access')
api.add_resource(UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(TokenRefresh, '/api/token/refresh')
api.add_resource(AllUsers, '/api/users')
api.add_resource(SecretResource, '/api/secret')
