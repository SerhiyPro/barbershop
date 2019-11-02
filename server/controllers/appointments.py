from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from server import api
from server.models import Appointments, Services, Users


class AppointmentsAll(Resource):
    def get(self):
        return {'appointments': list(map(lambda x: x.get_self_representation(), Appointments.get_all()))}, 200

    def post(self):
        data = get_parser_data(check=True)
        try:
            procedure_start_datetime = datetime.strptime(data['procedure_start_datetime'], '%Y-%m-%d %H:%M')
            procedure_end_datetime = datetime.strptime(data['procedure_end_datetime'], '%Y-%m-%d %H:%M')
        except ValueError:
            return {'message': 'Incorrect datetime format'}, 400

        if procedure_start_datetime > procedure_end_datetime:
            return {'message': 'Incorrect datetime input, start is bigger than end'}, 400

        service = Services.get_by_name_or_id(id=data['service'])
        if not service:
            return {'message': f'Service with id {data["service"]} does not exist'}, 400

        barber = Users.get_by_username_or_id(id=data['barber'])
        if not barber:
            return {'message': f'User with id {data["barber"]} does not exist'}, 400
        barber_appointments = Appointments.get_users_appointments(user_id=barber.id)
        procedure_day = procedure_start_datetime.date().strftime("%Y-%m-%d")
        if procedure_day in barber_appointments:
            for appointment in barber_appointments[procedure_day]:
                appointment_start = datetime.strptime(appointment['procedure_start_datetime'], '%Y-%m-%d %H:%M')
                appointment_end = datetime.strptime(appointment['procedure_end_datetime'], '%Y-%m-%d %H:%M')
                if procedure_start_datetime in get_datetime_range(start=appointment_start, end=appointment_end):
                    return {'message': 'Please choose another time for procedure'}, 400

        if data['comment']:
            new_appointment = Appointments(
                clients_name=data['clients_name'],
                clients_phone_number=data['clients_phone_number'],
                service=service.id,
                barber=barber.id,
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


class UserAppointments(Resource):
    def get(self, user_id):
        user = Users.get_by_username_or_id(id=user_id)
        if not user:
            return {'message': f'User with id {user_id} does not exist'}, 400

        return {'appointments': Appointments.get_users_appointments(user_id=user.id)}, 200


class Appointment(Resource):
    def get(self, id):
        appointment = Appointments.get_by_id(id)
        if not appointment:
            return {'message': f'Appointment with id {id} does not exist'}, 400

        return {'appointment': appointment.get_self_representation()}, 200

    @jwt_required
    def delete(self, id):
        appointment = Appointments.get_by_id(id)
        if not appointment:
            return {'message': f'Appointment with id {id} does not exist'}, 400

        appointment.delete_from_db()
        return {}, 202


def get_datetime_range(start=None, end=None):
    minutes = []
    while start < end:
        minutes.append(start)
        start += timedelta(minutes=1)
    return minutes


def get_parser_data(check=False):
    parser = reqparse.RequestParser()  # Adding request parses
    parser.add_argument('clients_name', help='This field cannot be blank', required=check)
    parser.add_argument('clients_phone_number', help='This field cannot be blank', required=check)
    parser.add_argument('service', type=int, help='This field cannot be blank and should be integer', required=check)
    parser.add_argument('barber', type=int, help='This field cannot be blank and should be integer', required=check)
    parser.add_argument('procedure_start_datetime', help='This field cannot be blank', required=check)
    parser.add_argument('procedure_end_datetime', help='This field cannot be blank', required=check)
    parser.add_argument('comment', required=False)
    return parser.parse_args()


api.add_resource(AppointmentsAll, '/api/appointments', methods=['GET', 'POST'])
api.add_resource(UserAppointments, '/api/appointments/user/<user_id>', methods=['GET'])
api.add_resource(Appointment, '/api/appointments/<id>', methods=['GET', 'PUT', 'DELETE'])
