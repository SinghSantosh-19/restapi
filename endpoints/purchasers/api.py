from config import db
from models.purchaser import Purchaser, PurchaserSchema

import json
from flask import abort
from flask_restful import Resource, reqparse


class PurchaserAPI(Resource):
    def get(self,id):
        # Get the person requested
        p = Purchaser.query.filter(Purchaser.id == id).one_or_none()
        # Did we find a person?
        if p is not None:
            # Serialize the data for the response
            p_schema = PurchaserSchema()
            data = json.dumps(p_schema.dump(p))
            return data
        else:
            # Otherwise, nope, didn't find that person
            abort(404,"Product not found for Id: {}".format(id),)

    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required = True)
        argname = parser.parse_args()

        if argname['name'] is None:
            abort(404,"Could not find purchaser name in message body!",)

        pname = argname['name']
        is_alredy_exists = Purchaser.query.filter(Purchaser.name == pname).one_or_none()
        if is_alredy_exists is not None:
            abort(404,"Purchaser:{} already exists with id: {}".format(is_alredy_exists.name, is_alredy_exists.id),)
        else:
            obj = Purchaser(name=pname)
            db.session.add(obj)
            db.session.commit()
            p_schema = PurchaserSchema()
            data = json.dumps(p_schema.dump(obj))
            return data

    def delete(self):
        pass