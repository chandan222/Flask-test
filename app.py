from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.item import Item,itemList
from resources.user import UserReister
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='chandan'
api=Api(app)
jwt=JWT(app,authenticate,identity)

@app.before_first_request
def create():
    db.create_all()



api.add_resource(Item,'/item/<string:name>')
api.add_resource(itemList,'/items')

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

api.add_resource(UserReister,'/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8080,debug=True)
