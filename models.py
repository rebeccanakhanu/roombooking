from sqlalchemy import create_engine, Column,Integer,Date,String,ForeignKey,Table
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy .ext.declarative import declarative_base


engine = create_engine('sqlite:///roombooking.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

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
        return f'<Room id={self.id}, room_number={self.room_number}>'

    def is_available(self, check_in_date, check_out_date):
        bookings = self.bookings
        for booking in bookings:
            if (
                check_in_date < booking.check_out_date
                and check_out_date > booking.check_in_date
            ):
                return False
        return True
    
    def get_available_rooms(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.query.all():
            if room.is_available(check_in_date, check_out_date):
                available_rooms.append(room)
        return available_rooms

    
class Customer(Base):
    __tablename__ = 'customers'
    
    id= Column(Integer(),primary_key= True)
    book_name= Column(String(250),nullable=False)
    phone_number=(Column(Integer(),nullable=False))
    email_address = Column(String(100),nullable=False)
    
    room = relationship("Room",uselist=False,back_populates="customer")
    bookings = relationship("Booking", back_populates="customer")

    def __repr__(self):
        return f'<Customer id={self.id}, name={self.book_name}>'

    def make_booking(self, room, check_in_date, check_out_date):
        if room.is_available(check_in_date, check_out_date):
            booking = Booking(
                room_id=room.id,
                customer_id=self.id,
                check_in_date=check_in_date,
                check_out_date=check_out_date
            )
            session.add(booking)
            session.commit()
            return booking
        else:
            return None

class Booking(Base):
   __tablename__ = 'bookings'

   id = Column(Integer(), primary_key=True)
   customer_id = Column(Integer, ForeignKey('customers.id'))
   check_in_date = Column(Date)
   check_out_date = Column(Date)
    
   customer = relationship("Customer", back_populates="bookings")
   def __repr__(self):
        return f'<Booking id={self.id}, customer_id={self.customer_id}>'

def is_current(self):
        today = Date.today()
        return self.check_in_date <= today <= self.check_out_date
    


