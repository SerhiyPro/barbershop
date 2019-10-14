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

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_self_representation(self):
        return {
            'id': self.id,
            'name': self.name,
            'photo': self.photo
        }

    def update(self, key, item):
        setattr(self, key, item)
        db.session.commit()

    @classmethod
    def get_by_name_or_id(cls, id=None, name=None):
        if name:
            return cls.query.filter_by(name=name).first()
        elif id:
            return cls.query.filter_by(id=id).first()

    @classmethod
    def return_all(cls):
        return cls.query.all()
