from app import db

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    pizza = db.relationship("Pizza", back_populates='orders')

    transactions = db.relationship("Transaction", back_populates='order')

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'client': self.client,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
