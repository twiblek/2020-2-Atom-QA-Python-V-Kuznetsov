from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

Base = declarative_base()

class Logs(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    asctime = Column(DateTime)
    name = Column(String)
    levelname = Column(String(10))
    levelno = Column(Integer)
    message = Column(String)

class Pets(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    kind = Column(String)
    is_male = Column(Boolean)