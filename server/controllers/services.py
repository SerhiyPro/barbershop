from server import api
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from server.models import Services


class ServicesAll(Resource):
    def get(self):
        return Services.get_all(), 200

    @jwt_required
    def post(self):
        data = get_parser_data(check=True)

        if Services.get_by_name_or_id(name=data['name']):
            return {'message': f'Service {data["name"]} already exists'}, 400

        new_service = Services(name=data['name'])
        new_service.save_to_db()
        return {
            'message': 'Service was successfully created',
            'service': {
                'id': new_service.id,
                'name': data['name']
            }
        }, 201


class Service(Resource):
    def get(self, id):

        service = Services.get_by_name_or_id(id=id)
        if not service:
            return {'message': f'Service with id {id} does not exist'}, 400

        return {'service': service.get_self_representation()}, 200

    @jwt_required
    def put(self, id):
        data = get_parser_data(check=True)
        service = Services.get_by_name_or_id(id=id)
        if not service:
            return {'message': f'Service with id {id} does not exist'}, 400

        service_update_info = {'name': data['name']}

        service.update(service_update_info)
        return {
            'message': 'Service was successfully updated',
            'service': {
                'id': service.id,
                'name': data['name']
            }
        }, 200

    @jwt_required
    def delete(self, id):
        service = Services.get_by_name_or_id(id=id)
        if not service:
            return {'message': f'Service with id {id} does not exist'}, 400

        service.delete_from_db()
        return {}, 202


def get_parser_data(check=False):
    parser = reqparse.RequestParser()
    parser.add_argument('name', help='This field cannot be blank', required=check)
    return parser.parse_args()


api.add_resource(ServicesAll, '/api/services', methods=['GET', 'POST'])
api.add_resource(Service, '/api/services/<id>', methods=['GET', 'PUT', 'DELETE'])
