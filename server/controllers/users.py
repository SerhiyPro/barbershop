import werkzeug
import uuid
import os
from flask import send_file
from flask_restful import Resource, reqparse
from server import api, jwt
from server.models import Users, Services
from server.models import RevokedTokenModel
from server.config import UPLOAD_FOLDER as UF
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, \
    jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

UPLOAD_FOLDER = os.path.join(UF, 'users')


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


class UserRegistration(Resource):
    def post(self):

        data = get_parser_data(check=True)

        if Users.get_by_username_or_id(username=data['username']):
            return {'message': f'User {data["username"]} already exists'}, 400

        photo = data['file']
        if not photo:
            return {'message': 'Incorrect photo provided'}, 400

        image_extension = photo.filename.split('.')[1]
        filename = f'{uuid.uuid4().hex}.{image_extension}'

        photo.save(os.path.join(UPLOAD_FOLDER, filename))
        if 'is_admin' in data:
            new_user = Users(
                username=data['username'],
                password_hash=Users.generate_hash(data['password']),
                photo=filename,
                full_name=data['full_name'],
                is_admin=True if data['is_admin'] in ('true', 'True', 1) else False
            )
        else:
            new_user = Users(
                username=data['username'],
                password_hash=Users.generate_hash(data['password']),
                photo=filename,
                full_name=data['full_name']
            )
        new_user.save_to_db()

        if 'services' in data:
            services_ids = (int(service_id) for service_id in data['services'] if service_id.isdigit())
            for service_id in services_ids:
                service = Services.get_by_name_or_id(id=service_id)
                if service:
                    new_user.add_service(service)

        access_token = create_access_token(identity=data['username'])  # to access protected routes
        refresh_token = create_refresh_token(identity=data['username'])  # to reissue access token after expiration
        return {
           'message': f'User {new_user.username} was successfully created',
           'user': new_user.get_self_representation(),
           'access_token': access_token,
           'refresh_token': refresh_token
        }, 201


class UserLogin(Resource):
    def post(self):
        data = get_login_parser_data()

        current_user = Users.get_by_username_or_id(username=data['username'])
        if not current_user:
            return {'message': f'User {data["username"]} doesn\'t exist'}, 400

        if not current_user.active:
            return {'message': 'User has been deactivated'}, 401

        if Users.verify_hash(data['password'], current_user.password_hash):
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
        refresh_token = create_refresh_token(identity=current_user)
        return {'access_token': access_token, 'refresh_token': refresh_token}, 200


class AllUsers(Resource):
    def get(self):
        return {'users': list(map(lambda x: x.get_self_representation(), Users.get_all()))}, 200


class User(Resource):
    def get(self, id):
        current_user = Users.get_by_username_or_id(id=id)
        if not current_user:
            return {'message': f'User with id {id} doesn\'t exist'}, 400
        return {'user': current_user.get_self_representation()}, 200

    @jwt_required
    def put(self, id):
        data = get_parser_data()

        current_user = Users.get_by_username_or_id(id=id)
        if not current_user:
            return {'message': f'User with id {id} doesn\'t exist'}, 400

        if data['username']:
            if Users.get_by_username_or_id(username=data['username']):
                return {'message': f'User with username {data["username"]} already exists'}, 400

        for key, value in data.items():
            if not value:  # in case no value provided
                continue
            if key == 'password':
                value = Users.generate_hash(data['password'])
            elif key == 'is_admin':
                value = True if data['is_admin'] in ('true', 'True', 1) else False
            elif key == 'services':
                current_user.services = []
                services_ids = [int(service_id) for service_id in data['services'] if service_id.isdigit()]
                for service_id in services_ids:
                    service = Services.get_by_name_or_id(id=service_id)
                    if service:
                        current_user.add_service(service)
                continue  # Go to the next iteration because add_service commits the changes
            elif key == 'file':
                photo = data['file']
                if not photo:
                    return {'message': 'Incorrect photo provided'}, 400
                image_extension = photo.filename.split('.')[1]
                filename = f'{uuid.uuid4().hex}.{image_extension}'
                photo.save(os.path.join(UPLOAD_FOLDER, filename))
                os.remove(os.path.join(UPLOAD_FOLDER, current_user.photo))
                value = filename
                key = 'photo'
            current_user.update(key, value)

        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])
        return {
            'user': current_user.get_self_representation(),
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 201

    @jwt_required
    def delete(self, id):
        current_user = Users.get_by_username_or_id(id=id)
        if not current_user:
            return {'message': f'User with id {id} doesn\'t exist'}, 400
        current_user.deactivate()
        return {}, 202


class UserProfilePhoto(Resource):
    def get(self, image_name):
        return send_file(os.path.join(os.getcwd(), UPLOAD_FOLDER, image_name))


def get_parser_data(check=False):
    parser = reqparse.RequestParser()
    parser.add_argument('username', help='This field cannot be blank', required=check)
    parser.add_argument('password', help='This field cannot be blank', required=check)
    parser.add_argument('full_name', help='This field cannot be blank', required=check)
    parser.add_argument('is_admin', required=False)
    parser.add_argument('services', required=False)
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files',
                        help='This field cannot be blank', required=check)
    return parser.parse_args()


def get_login_parser_data():
    parser = reqparse.RequestParser()
    parser.add_argument('username', help='This field cannot be blank', required=True)
    parser.add_argument('password', help='This field cannot be blank', required=True)
    return parser.parse_args()


api.add_resource(UserRegistration, '/api/registration', methods=['POST'])
api.add_resource(UserLogin, '/api/login', methods=['POST'])
api.add_resource(UserLogoutAccess, '/api/logout/access', methods=['POST'])
api.add_resource(UserLogoutRefresh, '/api/logout/refresh', methods=['POST'])
api.add_resource(TokenRefresh, '/api/token/refresh', methods=['POST'])
api.add_resource(AllUsers, '/api/users', methods=['GET'])
api.add_resource(User, '/api/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(UserProfilePhoto, '/uploads/users/<string:image_name>', methods=['GET'])
