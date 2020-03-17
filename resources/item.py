from flask_restful import Resource,reqparse
from flask_jwt import jwt_required


from models.item import ItemModel


class Item(Resource):
    parse=reqparse.RequestParser()
    parse.add_argument('price',
    type=float,required=True,help='This field is required')

    parse.add_argument('store_id',
    type=float,required=True,help='Every Item needs a store id')




    @jwt_required()
    def get(self,name):
        item=ItemModel.findbyname(name)
        if item is None:
            return {
            'message':'item not found'
        },404
        return item.json()




    @jwt_required()
    def post(self,name):
        item=ItemModel.findbyname(name)
        if item:
            return {'message':"Item with '{}' already exist".format(name)},400

        data=Item.parse.parse_args()
        item=ItemModel(name,**data)

        try:
            item.save_to_db()
        except:
            return {'message':'error occured while processing the insert'},500

        return item.json(),201

    @jwt_required()
    def delete(self,name):
        item=ItemModel.findbyname(name)
        if item is None:
            return {'message':"Item with '{}' does not exist".format(name)}, 400
        item.delete_from_db()

        return {'message':'Item with name {} is deleted'.format(name)}

    @jwt_required()
    def put(self,name):

        data=Item.parse.parse_args()
        item=ItemModel.findbyname(name)

        if item is None:
            item=ItemModel(name,**data)
        else:
            item.price=data['price']
            item.store_id=data['store_id']

        item.save_to_db()

        return item.json()


class itemList(Resource):
    @jwt_required()
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
