# -*- encoding: utf-8 -*-
"""
    File name: restaurant.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from flask_restful import Resource, marshal_with
from utils.fields.restaurant import restaurant_detail_fields, restaurant_simple_fields, restaurants_fields, pt_fields, delete_fields
from handler.restaurant import get_restaurant_by_id, get_all_restaurants, update_restaurant, rm_restaurant, create_restaurant
from utils.parsers.restaurant import restaurant_update_parser, restaurant_create_parser


class RestaurantsResource(Resource):
    @marshal_with(restaurants_fields)
    def get(self):
        restaurants = get_all_restaurants()
        return {'restaurants': restaurants}

    @marshal_with(pt_fields)
    def post(self):
        restaurant_args = restaurant_create_parser.parse_args()
        result = create_restaurant(
            restaurant_args.name, restaurant_args.description, restaurant_args.category_id,
            restaurant_args.phone, restaurant_args.address, restaurant_args.city,
            restaurant_args.country
        )
        return result


class RestaurantResource(Resource):
    @marshal_with(restaurant_detail_fields)
    def get(self, restaurant_id):
        restaurant = get_restaurant_by_id(restaurant_id)
        restaurant.category = restaurant.cuisine_category
        return restaurant

    @marshal_with(pt_fields)
    def put(self, restaurant_id):
        restaurant_args = restaurant_update_parser.parse_args()
        result = update_restaurant(
            restaurant_id, restaurant_args.name, restaurant_args.description,
            restaurant_args.phone, restaurant_args.address
        )
        return result

    @marshal_with(delete_fields)
    def delete(self, restaurant_id):
        result = rm_restaurant(restaurant_id)
        return result


