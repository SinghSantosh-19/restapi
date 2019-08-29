from endpoints.products.api import *
from config import api

# only POST requests on this
api.add_resource(ProductAPI, '/product','/product/', endpoint = 'Product', methods = ['POST'])

# only GET requests on this
api.add_resource(ProductAPI, '/product/<int:id>', '/product/<int:id>/', endpoint = 'products', methods = ['GET'])
