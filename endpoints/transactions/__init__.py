from endpoints.transactions.api import *
from config import api

# only post requests on this
api.add_resource(TransactionAPI,'/purchaser-product','/purchaser-product/', endpoint='purchaser-product', methods = ['POST'])

# only GET requests on this
api.add_resource(TransactionAPI,'/purchaser/<int:id>/product','/purchaser/<int:id>/product/', endpoint='transactions', methods = ['GET'])