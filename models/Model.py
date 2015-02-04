from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application import config

engine = create_engine(config.ENGINE_STRING, echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)
db_session = Session()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)
    location = Column(String)