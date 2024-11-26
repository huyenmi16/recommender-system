
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float,Enum
from sqlalchemy.orm import relationship
from ..config.connect_db import db

class User(db.Model):
    __tablename__ ='users'
    id = Column(Integer,primary_key = true)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum('male', 'female', 'other'))
    location = Column(String(255))


class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String(100),nullable=True)
    genre = Column(String(100))
    director = Column(String(100))
    actor = Column(String(255))
    price = Column(Float)



# Mô hình Label
class Label(db.Model):
    __tablename__ = 'labels'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rating = Column(Float)  # Điểm đánh giá
    is_liked = Column(Boolean)  # Thích/Không thích
    interaction_time = Column(DateTime)  # Thời gian tương tác

