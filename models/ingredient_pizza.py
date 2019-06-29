from sqlalchemy.orm import relationship, backref

from app import db

class IngredientPizza(db.Model):
    __tablename__ = "ingredient_pizza"

    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"))

    ingredient = relationship("Ingredient", backref=backref("ingredient"))
    pizza = relationship("Ingredient", backref=backref("ingredient"))
