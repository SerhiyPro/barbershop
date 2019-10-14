from datetime import datetime
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server import api
from server.models import Appointments, Services, Users


parser = reqparse.RequestParser()  # Adding request parses


class AppointmentsAll(Resource):
    # @jwt_required   TODO: uncomment
    def get(self):
        # Only for history and testing
        return {'appointments': list(map(lambda x: x.get_self_representation(), Appointments.return_all()))}, 200

    def post(self, ):
        parser.add_argument('clients_name', help='This field cannot be blank', required=True)
        parser.add_argument('clients_phone_number', help='This field cannot be blank', required=True)
        parser.add_argument('service', type=int, help='This field cannot be blank and should be integer', required=True)
        parser.add_argument('barber', type=int, help='This field cannot be blank and should be integer', required=True)
        parser.add_argument('procedure_start_datetime', help='This field cannot be blank', required=True)
        parser.add_argument('procedure_end_datetime', help='This field cannot be blank', required=True)
        parser.add_argument('comment', required=False)
        data = parser.parse_args()

        try:
            procedure_start_datetime = datetime.strptime(data['procedure_start_datetime'], '%Y-%m-%d %H:%M:%S')
            procedure_end_datetime = datetime.strptime(data['procedure_end_datetime'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return {'message': 'incorrect datetime format'}, 400

        if data['comment']:
            new_appointment = Appointments(
                clients_name=data['clients_name'],
                clients_phone_number=data['clients_phone_number'],
                service=data['service'],  # TODO: check if exists
                barber=data['barber'],
                procedure_start_datetime=procedure_start_datetime,
                procedure_end_datetime=procedure_end_datetime,
                comment=data['comment']
            )
        else:
            new_appointment = Appointments(
                clients_name=data['clients_name'],
                clients_phone_number=data['clients_phone_number'],
                service=data['service'],
                barber=data['barber'],
                procedure_start_datetime=procedure_start_datetime,
                procedure_end_datetime=procedure_end_datetime
            )

        new_appointment.save_to_db()
        return {
            'message': 'Appointment was successfully created',
            'appointment': new_appointment.get_self_representation()
        }, 201


class Appointment(Resource):
    def get(self, id):

        comment = Comments.get_by_id(id)
        if not comment:
            return {'message': f'Comment with id {id} does not exist'}, 400

        return {'comment': comment.get_self_representation()}, 200

    @jwt_required
    def put(self, id):
        parser.add_argument('commentators_name', required=False)
        parser.add_argument('value', required=False)
        parser.add_argument('rate', type=int, help='This field should be integer', required=False)
        parser.add_argument('is_checked', required=False)
        data = parser.parse_args()

        comment = Comments.get_by_id(id)
        if not comment:
            return {'message': f'Comment with id {id} does not exist'}, 400

        for key, value in data.items():
            if not value:
                continue
            if key == 'is_checked':
                value = True if value in ('true', 'True', 1) else False
            comment.update(key, value)

        return {
                   'message': 'Comment was successfully updated',
                   'comment': comment.get_self_representation()
        }, 200

    # @jwt_required  TODO: uncomment
    def delete(self, id):
        appointment = Appointments.get_by_id(id)
        if not appointment:
            return {'message': f'Appointment with id {id} does not exist'}, 400

        appointment.delete_from_db()
        return {}, 202


api.add_resource(AppointmentsAll, '/api/appointments', methods=['GET', 'POST'])
# api.add_resource(AppointmentsAll, '/api/comments/<string:user>', methods=['GET', 'POST'])
api.add_resource(Appointment, '/api/appointments/<id>', methods=['GET', 'PUT', 'DELETE'])
