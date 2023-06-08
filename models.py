
from sqlalchemy import create_engine, Column,Integer,Date,String,ForeignKey,Table
from sqlalchemy.orm import relationship
from sqlalchemy .ext.declarative import declarative_base

engine = create_engine('sqlite:///roombooking.db',echo=True)

Base = declarative_base()

# Define the association table for the many-to-many relationship between Room and Customer
room_customer_association = Table(
    'room_customer',
    Base.metadata,
    Column('room_id', Integer, ForeignKey('rooms.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)

class Room(Base):
    __tablename__ = 'rooms'
    
    id= Column(Integer(),primary_key= True)
    room_number = Column (String(250),nullable = False)
    room_type = Column (String(250),nullable = False)
    room_capacity = Column (Integer(),nullable = False)
    room_price = Column (Integer(),nullable = False)
    customer_id = Column(Integer, ForeignKey('customers.id'), unique=True)
    
    
    customer = relationship("Customer", uselist=False, back_populates="room")
    
    def __repr__(self):
        return f'Room'
    
    
class Customer(Base):
    __tablename__ = 'customers'
    
    id= Column(Integer(),primary_key= True)
    book_name= Column(String(250),nullable=False)
    phone_number=(Column(Integer(),nullable=False))
    email_address = Column(String(100),nullable=False)
    
    room = relationship("Room",uselist=False,back_populates="customer")
    bookings = relationship("Booking", back_populates="customer")

    def __repr__(self):
        return f'Customer'
    
    
class Booking(Base):
   __tablename__ = 'bookings'

   id = Column(Integer(), primary_key=True)
   customer_id = Column(Integer, ForeignKey('customers.id'))
   check_in_date = Column(Date)
   check_out_date = Column(Date)
    
   customer = relationship("Customer", back_populates="bookings")
    
       
    


