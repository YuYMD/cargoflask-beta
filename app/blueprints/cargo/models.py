from app.extensions import db
from datetime import datetime
    
    

class Mapping(db.Model):
    __tablename__ = 'mapping'

    prefix = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(20), nullable=False)
    spider_name = db.Column(db.String(10), nullable=False)



    
class Cargo_list(db.Model):
    __tablename__ = 'cargo_list'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    cargo_number = db.Column(db.String(12), db.ForeignKey('cargo_info.cargo_number'), primary_key=True)
    
    def __init__(self, id, cargo_number):
      self.id = id
      self.cargo_number = cargo_number
        

    def __repr__(self):
        return 'Cargo Number is {}'.format(self.cargo_number)
    
    

class Cargo_info(db.Model):
    __tablename__ = 'cargo_info'

    cargo_number = db.Column(db.Integer, primary_key=True)
    flight = db.Column(db.String(5))
    date = db.Column(db.DateTime, nullable=True)
    departure = db.Column(db.String(3))
    arrival = db.Column(db.String(3))
    pieces = db.Column(db.Integer)
    weight = db.Column(db.Numeric(6,1))
    std = db.Column(db.DateTime, nullable=True)
    sta = db.Column(db.DateTime, nullable=True)
    atd = db.Column(db.DateTime, nullable=True)
    ata = db.Column(db.DateTime, nullable=True)


    def __init__(self, cargo_number):
        self.cargo_number = cargo_number

    def __repr__(self):
        return 'Flight by {}'.format(self.flight)
