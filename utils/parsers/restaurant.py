# -*- encoding: utf-8 -*-
"""
    File name: restaurant.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from flask_restful import reqparse

# ------------ restaurant create parser ------------
restaurant_create_parser = reqparse.RequestParser()
restaurant_create_parser.add_argument(
    'name', dest='name',
    type=str, location='form',
    required=True, help="Please give a restaurant name"
)

restaurant_create_parser.add_argument(
    'description', dest='description',
    type=str, location='form',
    required=True, help="Please give a description"
)

restaurant_create_parser.add_argument(
    'category_id', dest='category_id',
    type=int, location='form',
    required=True, help="Please give a category id"
)

restaurant_create_parser.add_argument(
    'phone', dest='phone',
    type=str, location='form',
    required=True, help="Please give a phone number"
)

restaurant_create_parser.add_argument(
    'address', dest='address',
    type=str, location='form',
    required=True, help="Please give a address"
)

restaurant_create_parser.add_argument(
    'city', dest='city',
    type=str, location='form',
    required=True, help="This is the city where the restaurant locates"
)

restaurant_create_parser.add_argument(
    'country', dest='country',
    type=str, location='form',
    required=True, help="This is the country where the restaurant locates"
)


# ------------ restaurant update parser ------------
restaurant_update_parser = reqparse.RequestParser()


restaurant_update_parser.add_argument(
    'name', dest='name',
    type=str, location='form',
    required=False, help="Please give a new name"
)

restaurant_update_parser.add_argument(
    'description', dest='description',
    type=str, location='form',
    required=False, help="Please give an correct name"
)

restaurant_update_parser.add_argument(
    'phone', dest='phone',
    type=str, location='form',
    required=False, help="Please give a new phone number"
)

restaurant_update_parser.add_argument(
    'address', dest='address',
    type=str, location='form',
    required=False, help="Please give a new address"
)

