from server import db
from passlib.hash import pbkdf2_sha256 as sha256
from server.models.services import services_helper


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    services = db.relationship('Services', secondary=services_helper, lazy='subquery',
                               backref=db.backref('services', lazy=True))
    photo = db.Column(db.String(128))
    full_name = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def add_service(self, service):
        self.services.append(service)
        db.session.commit()

    def update(self, key, item):
        setattr(self, key, item)
        db.session.commit()

    def deactivate(self):
        self.active = False
        db.session.commit()

    @staticmethod
    def generate_hash(password: str):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, _hash):
        return sha256.verify(password, _hash)

    @classmethod
    def get_by_username_or_id(cls, id=None, username=None):
        if username:
            return cls.query.filter_by(username=username).first()
        elif id:
            return cls.query.filter_by(id=id).first()

    @classmethod
    def return_all(cls):
        return cls.query.all()
