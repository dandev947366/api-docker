import uuid

from flask import Flask, request
from flask_smorest import abort

from db import items, stores

app = Flask(__name__)

print("Hello from app")


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.post("/store/<string:name>/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    for store in stores:
        if store["name"] == name:
            new_item = {"name": item_data["name"], "price": item_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    abort(404, message="Store not found")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


if __name__ == "__main__":
    app.run(debug=True)
