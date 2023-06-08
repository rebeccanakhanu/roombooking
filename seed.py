from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Room,Customer,Booking

fake = Faker()

engine = create_engine('sqlite:///test.db')
session = sessionmaker(bind=engine)
session = session()

def seed_rooms():
    for _ in range(30):
        room = Room(
            room_number = fake.random_number(10),
            room_type = fake.word(),
            room_capacity = fake.random_int(min=1, max=2),
            room_price=fake.random_int(min=500,max=2500)
        )
session.add(Room)

session.commit()