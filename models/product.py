from datetime import datetime
from config import db, ma



class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, default=db.Sequence('trigger_id_seq'), primary_key=True)
    name = db.Column(db.String(255))
    created_timestamp = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)



class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
