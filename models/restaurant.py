# -*- encoding: utf-8 -*-
"""
    File name: restaurant.py
    Author: Jiaqi Xu <http:jqx.world>
"""
# The declarative extension in SQLAlchemy
# is the most recent method of using SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# class
class Restaurant(Base):
    # table
    __tablename__ = 'restaurant'

    # properties
    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('cuisine_category.category_id') )
    phone = Column(String(80), nullable=False)
    address = Column(String(80), nullable=False)
    city = Column(String(80), nullable=False)
    country = Column(String(80), nullable=False)
    addtime = Column(DateTime, nullable=False)


class CuisineCategory(Base):
    # table
    __tablename__ = 'cuisine_category'

    # properties
    category_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    Restaurants = relationship('Restaurant', backref='cuisine_category')






