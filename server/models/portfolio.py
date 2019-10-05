from server import db


class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    photo = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f'Portfolio work # {self.id}, description - {self.description}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
