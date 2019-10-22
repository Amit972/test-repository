import sqlite3
from section6.db import db


class UserModel(db.Model):
    TABLE_NAME = 'users'

    __tablename__ = "users"   # this is used by sqlalchemy to map object with the database. this must exist in the databse.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password
        # self.something = "hi"    # this is ignored by SQLAlchemy

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?" #.format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return cls.query.filter_by(username = username).first()   # here ist username is from database and 2nd one is parameter name and first() return the 1st row .

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id=?" #.format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return db.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
