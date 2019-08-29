
from config import db
from models.transaction import Transaction, TransactionSchema
from models.product import Product, ProductSchema
from models.purchaser import Purchaser, PurchaserSchema

import json
from flask import abort
from flask_restful import Resource, reqparse
from datetime import datetime
from sqlalchemy import desc

def convert_to_date(value):
    # TODO : can be enhanced to parse other formats of date (only date without time as well)
    d = datetime.strptime(value, '%Y/%m/%d %H:%M:%S')
    return d

class TransactionAPI(Resource):
    def get(self,id):
        # Get the person requested
        p = Purchaser.query.filter(Purchaser.id == id).one_or_none()
        # did we find the purchaser
        if p is not None:
            parser = reqparse.RequestParser()
            parser.add_argument('start_date', type=lambda x:datetime.strptime(x,'%Y/%m/%d %H:%M:%S'), required = False)
            parser.add_argument('end_date', type=lambda x:datetime.strptime(x,'%Y/%m/%d %H:%M:%S'), required = False)
            # above same can be done using simple function convert_to_date
            # parser.add_argument('start_date', type=convert_to_date, required = False)

            args = parser.parse_args()
            start_dates = args['start_date']
            end_dates = args['end_date']
            #if isinstance(start_dates, list) and len(start_dates) > 1:
            #    start_dates = datetime(1900,1,1)
            #if isinstance(end_dates, list) and len(start_dates) > 1:
            #    end_dates = datetime(3000,12,1)
            if start_dates is None:
                start_dates = datetime(1900,1,1)
            if end_dates is None:
                end_dates = datetime(3000,12,1)

            transactions = db.session.query(Transaction, Product).filter(
                Transaction.purchaser_id == id,
                Transaction.created_timestamp >= start_dates,
                Transaction.created_timestamp <= end_dates,
                Transaction.product_id == Product.id
                ).order_by(desc(Transaction.created_timestamp)).all()

            target = dict()
            for tr,pr in transactions:
                cur_date = tr.created_timestamp.date().strftime('%Y-%m-%d')
                if cur_date not in target:
                    target[cur_date] = []
                product_temp = {'product':pr.name}
                target[cur_date].append(product_temp)

            result_set = {'purchases':target}
            # Serialize the data for the response
            data = json.dumps(result_set)
            return data
        else:
            # Otherwise, nope didn't find the purchaser
            abort(404,'Purchaser not found for id : {}'.format(id),)


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('purchaser-id', type=int, required = True)
        parser.add_argument('product-id', type=int, required = True)
        parser.add_argument('purchased-timestamp', type=lambda x:datetime.strptime(x,'%Y/%m/%d %H:%M:%S'))
        args = parser.parse_args()

        if args['purchaser-id'] is None:
            abort(404, 'purchaser-id is mandatory!')
        if args['product-id'] is None:
            abort(404, 'product-id is mandatory!')
        purchased_timestamp = args['purchased-timestamp']
        if purchased_timestamp is None:
            purchased_timestamp = datetime.now

        is_already_exists = Transaction.query.filter(
            Transaction.purchaser_id == args['purchaser-id'],
            Transaction.product_id == args['product-id'],
            Transaction.created_timestamp == purchased_timestamp
            ).one_or_none()
        if is_already_exists is not None:
            ts = TransactionSchema()
            data = json.dumps(ts.dump(is_already_exists))
            abort(404,"Transaction already exists with id : {}".format(data),)
        else:
            p = Transaction(purchaser_id = args['purchaser-id']
                            , product_id = args['product-id']
                            , created_timestamp = purchased_timestamp
                            )
            db.session.add(p)
            db.session.commit()
            t_schema = TransactionSchema()
            data = json.dumps(t_schema.dump(p))
            return data

