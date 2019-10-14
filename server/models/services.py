from server import db

services_helper = db.Table(
    'services_helper',
    db.Column('service_id', db.Integer, db.ForeignKey('services.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)


class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'Service # {self.id}, name - {self.name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_self_representation(self):
        return {'id': self.id, 'name': self.name}

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    @classmethod
    def return_all(cls):
        return {'services': list(map(lambda x: {'id': x.id, 'name': x.name}, cls.query.all()))}

    @classmethod
    def get_by_name_or_id(cls, name=None, id=None):
        if name:
            return cls.query.filter_by(name=name).first()
        elif id:
            return cls.query.filter_by(id=id).first()
        else:
            return cls.quury.none()
