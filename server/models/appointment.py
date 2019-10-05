from server import db


class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    clients_name = db.Column(db.String(80))
    clients_phone_number = db.Column(db.String(12))
    service = db.Column(db.Integer, db.ForeignKey('services.id'), primary_key=True)
    barber = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    procedure_time = db.Column(db.DateTime)
    comment = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f'Appointment # {self.id}, by - {self.clients_name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
