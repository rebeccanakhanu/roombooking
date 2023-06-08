
from faker import Faker
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

from models import Booking, Customer, Room

fake = Faker()
random.seed(42)  # Set a seed for consistent random data

engine = create_engine('sqlite:///roombooking.db')
Session = sessionmaker(bind=engine)
session = Session()



def seed_bookings():
    rooms = session.query(Room).all()
    customers = session.query(Customer).all()
    bookings = []  # Empty list to hold added bookings

    if not rooms:
        print("No rooms found in the database.")
        return bookings  # Return empty list

    for _ in range(30):
        room = random.choice(rooms)
        customer = random.choice(customers)
        check_in_date = fake.date_between(start_date='today', end_date='+30d')
        check_out_date = check_in_date + timedelta(days=fake.random_int(min=1, max=7))

        booking = booking(
            room_id=room.id,
            customer_id=customer.id,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )
        session.add(booking)
        bookings.append(booking)  # Append the booking to the list

    session.commit()

    return bookings  # Return the list of added bookings
