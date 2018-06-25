from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT 
from resources.user import RegisterUser
from resources.item import Item , ItemList
from resources.store import Store , StoreList

from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

api.add_resource(Store , '/store/<string:name>')
api.add_resource(StoreList , '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(RegisterUser, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True) 
