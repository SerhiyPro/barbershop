import os
from server import app, db


@app.before_first_request
def create_tables():
    if not os.path.exists('db'):
        db.create_all()  # to create/use database


if __name__ == '__main__':
    app.run('0.0.0.0')
