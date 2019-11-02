from datetime import datetime
from itertools import groupby

from server import db


class Appointments(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clients_name = db.Column(db.String(80))
    clients_phone_number = db.Column(db.String(12))
    service = db.Column(db.Integer, db.ForeignKey('services.id'), primary_key=True)
    barber = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    procedure_start_datetime = db.Column(db.DateTime)
    procedure_end_datetime = db.Column(db.DateTime)
    comment = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f'Appointment # {self.id}, by - {self.clients_name}'

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_self_representation(self):
        return {
            'id': self.id,
            'clients_name': self.clients_name,
            'clients_phone_number': self.clients_phone_number,
            'service': str(self.service),
            'barber': str(self.barber),
            'procedure_start_datetime': str(self.procedure_start_datetime.strftime("%Y-%m-%d %H:%M")),
            'procedure_end_datetime': str(self.procedure_end_datetime.strftime("%Y-%m-%d %H:%M")),
            'comment': str(self.comment)
        }

    def update(self, key, item):
        setattr(self, key, item)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_users_appointments(cls, user_id):
        user_appointments = cls.query.filter_by(barber=user_id).filter(cls.procedure_start_datetime >= datetime.now()) \
            .order_by(cls.procedure_start_datetime)

        appointments = {}
        for day, appointments_time in groupby(user_appointments,
                                              lambda app: app.procedure_start_datetime.date().strftime("%Y-%m-%d")):
            if day not in appointments:
                appointments[day] = []
            for appointment_time in appointments_time:
                appointments[day].append(
                    {
                        'procedure_start_datetime': appointment_time.procedure_start_datetime.strftime("%Y-%m-%d %H:%M"),
                        'procedure_end_datetime': appointment_time.procedure_end_datetime.strftime("%Y-%m-%d %H:%M"),
                    })
        return appointments
