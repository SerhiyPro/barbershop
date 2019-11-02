import werkzeug
import uuid
import os
from flask import send_file
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server import api
from server.models import WorkSpheres
from server.config import UPLOAD_FOLDER as UF

parser = reqparse.RequestParser()  # Adding request parses
UPLOAD_FOLDER = os.path.join(UF, 'work_spheres')


class WorkSpheresAll(Resource):
    def get(self):
        return {'work_spheres': list(map(lambda x: x.get_self_representation(), WorkSpheres.get_all()))}, 200

    @jwt_required
    def post(self):
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files',
                            help='This field cannot be blank', required=True)
        parser.add_argument('name', help='This field cannot be blank', required=True)
        data = parser.parse_args()

        if WorkSpheres.get_by_name_or_id(name=data['name']):
            return {'message': f'Work sphere {data["name"]} already exists'}, 400

        photo = data['file']
        if not photo:
            return {'message': 'Incorrect photo provided'}, 400

        image_extension = photo.filename.split('.')[1]
        filename = f'{uuid.uuid4().hex}.{image_extension}'

        photo.save(os.path.join(UPLOAD_FOLDER, filename))

        new_work_sphere = WorkSpheres(name=data['name'], photo=filename)
        new_work_sphere.save_to_db()
        return {
            'message': 'Work sphere was successfully created',
            'work_sphere': new_work_sphere.get_self_representation()
        }, 201


class WorkSphere(Resource):
    def get(self, id):

        work_sphere = WorkSpheres.get_by_name_or_id(id=id)
        if not work_sphere:
            return {'message': f'Work sphere with id {id} does not exist'}, 400

        return {'service': work_sphere.get_self_representation()}, 200

    @jwt_required
    def put(self, id):
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=False)
        parser.add_argument('name', required=False)
        data = parser.parse_args()

        work_sphere = WorkSpheres.get_by_name_or_id(id=id)
        if not work_sphere:
            return {'message': f'Work sphere with id {id} does not exist'}, 400

        for key, value in data.items():
            if not value:
                continue
            if key == 'file':
                photo = data['file']
                if not photo:
                    return {'message': 'Incorrect photo provided'}, 400
                image_extension = photo.filename.split('.')[1]
                filename = f'{uuid.uuid4().hex}.{image_extension}'
                photo.save(os.path.join(UPLOAD_FOLDER, filename))
                os.remove(os.path.join(UPLOAD_FOLDER, work_sphere.photo))
                value = filename
                key = 'photo'
            work_sphere.update(key, value)

        return {
            'message': 'Work sphere was successfully updated',
            'work_sphere': work_sphere.get_self_representation()
        }, 200

    @jwt_required
    def delete(self, id):
        work_sphere = WorkSpheres.get_by_name_or_id(id=id)
        if not work_sphere:
            return {'message': f'Work sphere with id {id} does not exist'}, 400

        work_sphere.delete_from_db()
        return {}, 202


class WorkSpherePhoto(Resource):
    def get(self, image_name):
        return send_file(os.path.join(os.getcwd(), UPLOAD_FOLDER, image_name))


api.add_resource(WorkSpheresAll, '/api/work_spheres', methods=['GET', 'POST'])
api.add_resource(WorkSphere, '/api/work_spheres/<id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(WorkSpherePhoto, '/uploads/work_spheres/<string:image_name>')
