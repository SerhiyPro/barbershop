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

    def __repr__(self):
        return f'<User {self.username}>'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def generate_hash(password: str):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, _hash):
        return sha256.verify(password, _hash)

    @classmethod
    def get_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password_hash,
                'services': str(x.services)
            }

        return {'users': list(map(lambda x: to_json(x), cls.query.all()))}