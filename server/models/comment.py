from server import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    commentators_name = db.Column(db.String(80))
    value = db.Column(db.String(120))
    rate = db.Column(db.SmallInteger)
    is_checked = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f'Comment # {self.id}, by - {self.commentators_name}'

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
