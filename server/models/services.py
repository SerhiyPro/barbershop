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

    @classmethod
    def get_by_name(cls, name: str):
        return cls.query.filter_by(name=name).first()
