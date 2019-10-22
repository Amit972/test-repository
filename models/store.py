from section6.db import db


class StoreModel(db.Model):
    __tablename__ = "stores"  # this is used by sqlalchemy to map object with the database. this must exist in  data bse.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship("ItemModel",lazy="dynamic")  #  to stop sqlalchemy to ctrreate object for each item in database
    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'item': [x.json() for x in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # this is sqlAlchemy which is similar to select * from items where name=name this is returning ItemModel object

    def save_to_db(self):  # def insert (Self):
        db.session.add(self)  # session is the collection of object that we write into the database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

