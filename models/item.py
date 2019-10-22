import sqlite3
from section6.db import db
# models are used to help resources to make restful api


class ItemModel(db.Model):
    __tablename__ = "items"  # this is used by sqlalchemy to map object with the database. this must exist in the databse.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # for the security purpose
    store = db.relationship("StoreModel")  # sqlalchemy doesn't allow us for the sql joins

    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        # print(self.price, self.name)

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # # connection.close()
        #
        # if row:
        #     return cls(*row)
        return cls.query.filter_by(name=name).first()  # this is sqlAlchemy which is similar to select * from items where name=name this is returning ItemModel object
        #  or .filter_by(id=1) / filter_by(name=name,id=1)

    def save_to_db(self):  # def insert (Self):
        # print(1)
        # connection = sqlite3.connect('data.db')
        # print(2)
        # cursor = connection.cursor()
        # print(3)
        # query = "INSERT INTO items VALUES(?, ?)"     #.format(table=self.TABLE_NAME)
        # print(4)
        # cursor.execute(query, (self.name, self.price))
        # print(5)
        # connection.commit()
        # connection.close()
        # sqlalchemy can directly translate model object into row
        db.session.add(self)  #session is the collection of object that we write into the database
        db.session.commit()
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "UPDATE items SET price=? WHERE name=?"    #.format(table=self.TABLE_NAME)
    #     cursor.execute(query, (self.name, self.price))
    #
    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

