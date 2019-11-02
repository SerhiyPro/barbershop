from server import db


class Comments(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    commentators_name = db.Column(db.String(80))
    value = db.Column(db.String(120))
    rate = db.Column(db.SmallInteger)
    is_checked = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'Comment # {self.id}, by - {self.commentators_name}'

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_self_representation(self):
        return {
            'id': self.id,
            'commentators_name': self.commentators_name,
            'value': self.value,
            'rate': self.rate,
            'is_checked': self.is_checked
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
