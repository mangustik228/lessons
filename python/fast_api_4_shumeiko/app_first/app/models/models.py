from app.config.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class Seller(Base):
    __tablename__ = "seller"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    legal_adress = Column(String, nullable=True)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
