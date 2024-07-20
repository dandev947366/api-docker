import uuid

from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
