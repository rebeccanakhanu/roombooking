from squalalchemy import cclumn,Integer,String,ForeignKey
from squalaalchemy.orm import relationship
from squalalchemy .ext.declarative import declarative_base

engine = create_engine('sqlite:///roombooking.db',echo=True)

Base = declarative_base()


