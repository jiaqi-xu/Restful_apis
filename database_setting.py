# -*- encoding: utf-8 -*-
"""
    File name: database_setting.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from sqlalchemy import create_engine
from models.restaurant import Restaurant, Base, CuisineCategory

# configuration
engine = create_engine("mysql+pymysql://root:root@localhost:8889/apis")
Base.metadata.create_all(engine)
