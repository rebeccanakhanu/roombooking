# debug.py
import ipdb

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Room,Booking,Customer
from faker import Faker
if __name__ == "__main__":
    
    engine = create_engine('sqlite:///roombooking.db',echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    fake=Faker()


# Start the debugging session
ipdb.set_trace()
    



