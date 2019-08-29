from endpoints.purchasers.api import *
from config import api

# only POST requests on this
api.add_resource(PurchaserAPI,'/purchaser','/purchaser/', endpoint='purchaser', methods = ['POST'])

# only GET requests on this
api.add_resource(PurchaserAPI, '/purchaser/<int:id>', '/purchaser/<int:id>/', endpoint = 'purchasers', methods = ['GET'])