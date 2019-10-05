from server import db


class WorkSpheres(db.Model):
    __tablename__ = 'work_spheres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True, nullable=False)
    photo = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f'Work sphere # {self.id}, name - {self.name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_name(cls, name: str):
        return cls.query.filter_by(name=name).first()
