RoomBooking
RoomBooking is a CLI application that allows users to manage room bookings for a hotel or similar establishment.
The project utilizes Python and click for creating, modifying, and querying bookings.

Installation
To use RoomBooking, follow these steps:
Clone the project repository from GitHub.
Navigate to the project directory.
Install the required dependencies by running the following command:
pipenv install
Activate the virtual environment using the following command:
pipenv shell
Run the CLI application by executing the following command:
python cli.py
Dependencies
RoomBooking relies on the following external libraries:

SQLAlchemy: Used for object-relational mapping (ORM) to interact with the database.
Click: Provides a framework for building command-line interfaces.
Alembic: A database migration tool for SQLAlchemy.
Database Schema
The project uses SQLAlchemy ORM to define and manage the database schema. The schema includes three main tables:

Rooms: Represents the available rooms in the establishment. Contains information such as room number, type, capacity, and price.
Customers: Stores customer details, including name, phone number, and email.
Bookings: Tracks the bookings made by customers, including check-in and check-out dates.
The database schema design is implemented in the models.py file, which contains the SQLAlchemy model definitions for each table.

Usage
The RoomBooking CLI application offers the following functionality:

Creating new bookings: Users can create bookings by specifying the room, customer, and check-in/check-out dates.
Managing bookings: Users can modify and cancel existing bookings.
Checking room availability: Users can check if a room is available for a specific date range.
Retrieving booking details: Users can view information about their bookings, including current, past, and upcoming bookings.
The CLI follows best practices and provides detailed prompts and messages throughout the execution. It also incorporates validation for user input to ensure data integrity.

DSA Execution
The RoomBooking project incorporates the use of lists, tuples, and dictionaries within the CLI application. Additionally, it utilizes one or more algorithms from the Data Structures and Algorithms (DSA) module in appropriate contexts. These elements enhance the functionality and efficiency of the application.

CLI Best Practices
The CLI application separates scripted elements from object-oriented code, adhering to best practices. It validates user input to prevent errors and provides detailed prompts and messages to guide users through the booking process. The project also leverages external libraries to minimize project-specific code, promoting maintainability and reusability.

Configuration of Environment and Dependencies
The project uses Pipenv to manage its environment and dependencies. The Pipfile included in the project contains all the necessary dependencies and excludes any unneeded ones. The package structure is organized in a way that allows project files to be used in every project directory, ensuring modularity and easy access to required modules.

This project was developed as part of Phase 3 of the course and demonstrates proficiency in various concepts covered throughout the phase, including Python fundamentals, SQL, object-oriented programming, ORM, and CLI design.

The project is private and was worked by Rebecca Wakhungu.


