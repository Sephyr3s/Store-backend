from sqlalchemy import Column, Integer, String
from app.database.session import Base

class Place(Base):
    __tablename__ = "places"
    id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String, index=True)
    precio = Column(Integer)
    imagen = Column(String)
