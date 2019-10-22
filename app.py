from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from section6.security import authenticate, identity
from section6.resources.user import UserRegister
from section6.resources.item import Item,ItemList
from section6.resources.store import Store,StoreList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'amit'   # private key used by jwt to generate token

# using sql alchemy we can tell the python where to define data.db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # live at the root of the project

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # this is tracker which track all the modification done to the database. this is flask_sqlalchemy track which is turned off because sqlalchemy has its own tracker.


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # things required to generate token.
api = Api(app)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from section6.db import db  # circular import
    db.init_app(app)
    app.run(debug=True,port=1)  # important to mention debug=True