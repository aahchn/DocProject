from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

     # model will these 3 columns - tells SQLAlchemy how to read these tables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    #name, price and store_id will be passed into here from tablename above
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  #.query is from db.Model (SQLALchemy)
        # same as SELECT * FROM items WHERE name = name LIMIT 1 (return only the first result)

    def save_to_db(self):  #insert method
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):  #delete method
        db.session.delete(self)
        db.session.commit()
