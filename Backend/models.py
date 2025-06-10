from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True, ) 
    last_name = Column(String, index=True, ) 