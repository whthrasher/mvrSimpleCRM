import os
from sqlalchemy import \
    Column, \
    String, \
    Integer, \
    DateTime, \
    create_engine
from flask_sqlalchemy import \
    SQLAlchemy
import json

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_name = "mvrdb"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()

'''
Business
'''
class Business(db.Model):
  __tablename__ = 'businesses'

  id = Column(Integer, primary_key=True)
  date_added = Column(DateTime, nullable=False)
  name = Column(String, nullable=False)
  description = Column(String)

  def __init__(self, name, description, date_added):
    self.name = name
    self.description = description
    self.date_added = date_added

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'added': self.date_added,
      'name': self.name,
      'description': self.description}


'''
members
'''
class Member(db.Model):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    date_added = Column(DateTime, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    membership_type = Column(String, nullable=False)
    address = Column(String)
    city = Column(String(120))
    state = Column(String(120))
    phone = Column(String(120))
    email_address = Column(String(120))

    def __init__(self, first_name, last_name, membership_type, address,
                 city, state, phone, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type
        self.address = address
        self.city = city
        self.state = state
        self.phone = phone
        self.email_address = email_address

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.first_name + ' ' + self.last_name,
            'address': self.address + ' ' + self.city + ', ' + self.state,
            'phone': self.phone,
            'email_address': self.email_address
        }

'''
bm_rel
'''

class Customer_Relationship(db.Model):
    __tablename__ = 'customer_relationships'

    id = Column(Integer, primary_key=True)
    date_added = Column(db.DateTime, nullable=False)
    business_id = Column(db.Integer, db.ForeignKey('businesses.id'),
                         nullable=False)
    member_id = Column(db.Integer, db.ForeignKey('members.id'),
                       nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    membership_type = Column(String)

    def __init__(self, business_id, member_id, active, membership_type):
        self.business_id = business_id
        self.member_id = member_id
        self.active = active
        self.membership_type = membership_type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'member_id': self.member_id,
            'active': self.active,
            'membership_type': self.membership_type,
            'date_added': self.date_added
        }


