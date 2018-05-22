# -*- encoding: utf-8 -*-
"""
    File name: restaurant.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from flask_restful import fields


category_fields = {
    'category_id': fields.Integer,
    'name': fields.String
}

# for get /restaurants/<restaurant_id>
restaurant_detail_fields = {
    'restaurant_id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'category': fields.Nested(category_fields),
    'phone': fields.String,
    'address': fields.String,
    'city': fields.String,
    'country': fields.String,
    'addtime': fields.DateTime
}

pt_fields = {
    'restaurant_id': fields.String,
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}

delete_fields = {
    'restaurant_id': fields.String,
    'success': fields.Integer(default=0),
    'message': fields.String(default='No message'),
}


# for get /restaurants
restaurant_simple_fields = {
    'restaurant_id': fields.Integer,
    'name': fields.String
}

restaurants_fields = {
    'restaurants': fields.List(fields.Nested(restaurant_simple_fields))
}





