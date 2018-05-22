# -*- encoding: utf-8 -*-
"""
    File name: restaurant.py
    Author: Jiaqi Xu <http:jqx.world>
"""
from flask import abort
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.restaurant import Restaurant, Base, CuisineCategory

engine = create_engine("mysql+pymysql://root:root@localhost:8889/apis")
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_all_restaurants():
    restaurants = session.query(
        Restaurant
    ).order_by(Restaurant.restaurant_id).all()

    return restaurants


def get_restaurant_by_id(restaurant_id):
    '''
    restaurant = (
        session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    )

    category = (
        session.query(CuisineCategory).filter_by(
            category_id=restaurant.category_id
        )
    )
    '''
    result = session.query(Restaurant).join(
        CuisineCategory,
        Restaurant.category_id == CuisineCategory.category_id
    ).filter(
        Restaurant.restaurant_id == restaurant_id
    ).one()
    return result


def update_restaurant(restaurant_id, name, description, phone, address):
    restaurant = (
        session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    )

    if restaurant is None:
        return {'message': 'The restaurant does not exist.'}

    if name is not None:
        restaurant.name = name

    if description is not None:
        restaurant.description = description

    if phone is not None:
        restaurant.phone = phone

    if address is not None:
        restaurant.address = address

    session.add(restaurant)
    session.commit()
    return {
        'restaurant_id': restaurant.restaurant_id,
        'success': 1,
        'message': 'update successfully.'
    }


def rm_restaurant(restaurant_id):
    restaurant = (
        session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    )

    if restaurant is None:
        return {'message': 'The restaurant does not exist.'}

    session.delete(restaurant)
    session.commit()
    return {
        'restaurant_id': restaurant.restaurant_id,
        'success': 1,
        'message': 'delete successfully.'
    }


def create_restaurant(
        name, description, category_id, phone, address, city, country
):
    restaurant = Restaurant(
        name=name,
        description=description,
        category_id=category_id,
        phone=phone,
        address=address,
        city=city,
        country=country,
        addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    session.add(restaurant)
    session.commit()
    return {
        'restaurant_id': restaurant.restaurant_id,
        'success': 1,
        'message': 'create successfully.'
    }





