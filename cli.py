import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models import Customer, Room,Booking
Base = declarative_base()
engine=create_engine("sqlite:///roombooking.db")
Session = sessionmaker(bind=engine)
session = Session()
@click.group()
def cli():
    pass
@cli.command()
@click.option("--book_name", prompt="enter book name")
@click.option("--phone_number", prompt="enter phone number")
@click.option("--email", prompt="enter email")
def add_customer(book_name, phone_number, email):
    customer = Customer(book_name=book_name, phone_number=phone_number, email=email)
    session.add(customer)
    session.commit()
    print("Customer added successfully")
@cli.command()  
@click.option("--room_number", prompt="enter room number")
@click.option("--room_type", prompt="enter room type")
@click.option("--room_capacity", prompt="enter room capacity")
@click.option("--room_price", prompt="enter room price")
def add_room(room_number, room_type, room_capacity, room_price):
    room = Room(room_number=room_number, room_type=room_type, room_capacity=room_capacity, room_price=room_price)
    session.add(room)
    session.commit()
    print("Room added successfully")
@cli.command()
@click.option("--customer_id",prompt = "Customer id")
@click.option ("--check_in_date",prompt ="check in date")
@click.option ("--check_out_date",prompt ="check out date")
def book_room(customer_id, check_in_date, check_out_date):
    booking = Booking(customer_id=customer_id, check_in_date=check_in_date, check_out_date=check_out_date)
    session.add(booking)
    session.commit()
    print("Room booked successfully")
cli.add_command(add_customer)   
cli.add_command(add_room)
cli.add_command(book_room)
if __name__ == "__main__":
    cli()
    