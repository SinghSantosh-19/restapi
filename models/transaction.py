from datetime import datetime
from config import db, ma


class Transaction(db.Model):
    __tablename = "transaction"
    transaction_id = db.Column(db.Integer, default=db.Sequence('trigger_id_seq'), primary_key=True)
    purchaser_id = db.Column(db.Integer, db.ForeignKey("purchaser.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TransactionSchema(ma.ModelSchema):
    class Meta:
        model = Transaction