from app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String, nullable=False)
    pizza = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=func.current_timestamp())

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'client': self.client,
            'pizza': self.pizza,
            'created_at': self.created_at,
            'updated_at': self.updated_at_at
        }
