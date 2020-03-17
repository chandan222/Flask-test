from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self,name):
        store=StoreModel.findbyname(name)

        if store:
            return store.json()

        return {'message':'No stores found'},404


    def post(self,name):
        store=StoreModel.findbyname(name)
        if store:
            return  {'message':' store with name {} already exist'.format(name)}
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'unable to add store'},500
        return store.json(),201


    def delete(self,name):
        store=StoreModel.findbyname(name)
        if store:
            store.delete_from_db()
        else:
            return {'message':'store does not exist'}

        return {'message':'store deleted'},


class StoreList(Resource):

    def get(self):
        return {'store': [store.json() for store in StoreModel.query.all()]}
