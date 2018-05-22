# -*- encoding: utf-8 -*-
"""
    File name: runner.py
    Author: Jiaqi Xu <http:jqx.world>
"""

from flask import Flask
from app import restaurant_bp

app = Flask(__name__)
app.register_blueprint(restaurant_bp, url_prefix="/v1")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)