# -*- encoding: utf-8 -*-
"""
    File name: app.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from flask import Blueprint
from flask_restful import Api
from resources.restaurant import RestaurantResource, RestaurantsResource

restaurant_bp = Blueprint("restaurant", __name__)
api = Api(restaurant_bp)

api.add_resource(RestaurantResource, '/restaurants/<restaurant_id>')
api.add_resource(RestaurantsResource, '/restaurants/')
