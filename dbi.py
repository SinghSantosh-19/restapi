import os
from datetime import datetime
from config import db
from models.product import Product
from models.purchaser import Purchaser
from models.transaction import Transaction


def initialize_db():
    # Delete database file if it exists currently
    if os.path.exists("test.db"):
        os.remove("test.db")

    # Create the database
    db.create_all()

    # Data to initialize database with
    products = [
        {"id": 1, "name": "shoe"},
        {"id": 2, "name": "shirt"},
        {"id": 3, "name": "pant"},
    ]

    purchasers = [
        {"id": 1, "name": "Ashwin"},
        {"id": 2, "name": "Kohli"},
        {"id": 3, "name": "Pant"},
    ]

    transactions = [
        {"transaction_id":1, "purchaser_id":1, "product_id":1, "timestamp":'2019/08/26 23:59:59' },
        {"transaction_id":2, "purchaser_id":1, "product_id":2, "timestamp":'2019/08/28 00:59:59' },
        {"transaction_id":3, "purchaser_id":1, "product_id":3, "timestamp":'2019/08/26 10:00:00' }
    ]

    # iterate over the Product structure and populate the database
    for each_p in products:
        p = Product(id=each_p.get("id"), name=each_p.get("name"))
        db.session.add(p)

    for each_p in purchasers:
        p = Purchaser(id=each_p.get("id"), name=each_p.get("name"))
        db.session.add(p)

    for each_p in transactions:
        p = Transaction(transaction_id=each_p.get("transaction_id")
                        , purchaser_id=each_p.get("purchaser_id")
                        , product_id=each_p.get("product_id")
                        , created_timestamp=datetime.strptime(each_p.get("timestamp"), '%Y/%m/%d %H:%M:%S')
                        )
        db.session.add(p)

    db.session.commit()


