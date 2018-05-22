# -*- encoding: utf-8 -*-
"""
    File name: sample_data.py
    Author: Jiaqi Xu <http:jqx.world>
"""
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from database_setting import Restaurant, Base, CuisineCategory

engine = create_engine("mysql+pymysql://root:root@localhost:8889/apis")
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Chinese Cuisine
# 注意，得加这个实例，才可以插入restaurant数据，因为外键依赖
cuisine_category_1 = CuisineCategory(
    name="Chinese Cuisine"
)

session.add(cuisine_category_1)
session.commit()

cuisine_category_2 = CuisineCategory(
    name="Hotpot"
)
session.add(cuisine_category_2)
session.commit()

cuisine_category_3 = CuisineCategory(
    name="Barbecue"
)
session.add(cuisine_category_3)
session.commit()

cuisine_category_4 = CuisineCategory(
    name="SeaFood"
)
session.add(cuisine_category_4)
session.commit()
'''
'''
# Full House
restaurant_1 = Restaurant(
    name="Full House",
    description=(
        "Modern, informal restaurant for classic specialties from "
        "Jiangxi, Sichuan & other Chinese regions."
    ),
    category_id=1,
    phone="(613)798-5697",
    address="1766 Carling Ave, Ottawa, ON K2A 1E1",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_1)
session.commit()

# OpenRice
restaurant_2 = Restaurant(
    name="OpenRice",
    description=(
        "OpenRice Asian Fusion & Lounge in Ottawa offers the best of "
        "Korean, Vietnamese, Thaï and Chinese cuisine."
    ),
    category_id=1,
    phone="(613)739-8833",
    address="1755 St Laurent Blvd, Ottawa, ON K1G 3V4",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_2)
session.commit()

# Gyu-Kaku Japanese BBQ 牛角烤肉
restaurant_3 = Restaurant(
    name="Gyu-Kaku Japanese BBQ",
    description=(
        "Gyu-Kaku is a chain of Japanese yakiniku "
        "restaurants specializing in Japanese barbecue."
    ),
    category_id=3,
    phone="(514)866-8808",
    address="1255 Crescent St, Montreal, QC H3G 2B1",
    city="Montreal",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_3)
session.commit()

# 刘一手 Liuyishou Hotpot
restaurant_4 = Restaurant(
    name="Liuyishou Hotpot",
    description=(
        "Liuyishou Hotpot was founded in 2000, and throughout the past 17 years the entire team has continued to move "
        "forward by constantly honing their skills, evolving from a single hot pot restaurant on a small street to a franchise "
        "of over 1000 locations throughout the world. Liuyishou restaurants can be found throughout China, as well as in Canada, "
        "USA, Dubai, Singapore, Australia, Japan, Thailand, and France. Liuyishou\'s fashionably healthy image, "
        "outstanding quality and authentic hot pot taste and culture have garnered the favour of countless cuisine lovers."
    ),
    category_id=2,
    phone="(613)680-0188",
    address="10-1568 Merivale Rd, Nepean, ON K2G 3J9",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_4)
session.commit()


# 德庄 Moral Village HotPot
restaurant_5 = Restaurant(
    name="Moral Village Hotpot",
    description=(
        "Morals Village of Canada is based on Chinese Famous Cuisine brand (Moral Village); "
        "with bringing the new style hot pot integrates into foreign cuisine elements aim to "
        "create a unique boutique hot pot culture from its products, services and the environment."
    ),
    category_id=2,
    phone="(613)736-6503",
    address="3987 Riverside Dr Unit 1, Ottawa, ON K1V 1C1",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_5)
session.commit()

# Little Sheep Mongolian HotPot, 小肥羊
restaurant_6 = Restaurant(
    name="Little Sheep Mongolian HotPot",
    description=(
       "Little Sheep is a restaurant chain with a mission to introduce Mongolian culture and "
       "food in North America. With over 30 locations spread throughout North America, Little Sheep "
       "specializes in a traditional Inner Mongolian hot pot cuisine featuring tabletop cooking served "
       "in a metal pot filled with herbs and spices."
    ),
    category_id=2,
    phone="(613)248-3388",
    address="1514 Merivale Rd #15, Nepean, ON K2G 3J6",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_6)
session.commit()

# Captain's Boil
restaurant_7 = Restaurant(
    name="Captain\'s Boil",
    description=(
      "The Captain\'s Boil was inspired by Cajun seafood boil, where freshly caught"
      " seafood is boiled and served right away to retain its freshness and tenderness. "
      "The Captain\'s Boil took this idea further by adding aromatic Asian spices to enhance the "
      "natural taste of our ingredients. By removing all the unnecessary hassle of table settings and "
      "cutlery, we make sure that the food is ready-to-eat from sea to table. "
    ),
    category_id=4,
    phone="(613)680-8998",
    address="290 W Hunt Club Rd #4b, Ottawa, ON K2E 0B7",
    city="Ottawa",
    country="Canada",
    addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

session.add(restaurant_7)
session.commit()




