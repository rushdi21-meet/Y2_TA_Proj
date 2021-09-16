from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
