from app import app
from flask import jsonify, request
from flask_cors import cross_origin
from sqlalchemy import create_engine

from flask_marshmallow import Marshmallow

import pymysql


@app.route("/available-item", methods=['GET'])
@cross_origin()
def itemList():
    items = {
        "Available": "Item list",
        "items":[
            {"Coke":"Nu: 25"},
            {"chips":"Nu: 20"},
            {"chocolate": "Nu: 5"}
        ]
    }
    return jsonify(items)

@app.route("/item", methods=['POST'])
@cross_origin()
def getItem():
    json_request = request.json
    item_name = json_request['item_name']
    quantity = json_request['quantity']
    amt = json_request['amount']

    items = ["coke","chips", "chocolate"]
    if (item_name in items):
        if(item_name == "coke"):
            cost = int(quantity) * 25
            if(int(amt) == cost):
                return jsonify({"Your Choice":"Coke",  "Quantity": quantity})
            elif(amt>cost):
                blance = int(amt)-cost
                return jsonify({"Your Choice":"Coke",  "Quantity": quantity, "Your Blance": blance})
            else:
                return jsonify({"message":"Insufficient Amount", "Take Back your money":amt})
        elif(item_name == "chips"):
            cost = int(quantity) * 20
            if(int(amt) == cost):
                return jsonify({"Your Choice":"Chips", "Quantity": quantity})
            elif(amt>cost):
                blance = int(amt)-cost
                return jsonify({"Your Choice":"Chips", "Quantity": quantity, "Your Blance": blance})
            else:
                return jsonify({"message":"Insufficient Amount", "Take Back your money":amt})

        elif(item_name == "chocolate"):
            cost = int(quantity) * 5
            if(int(amt) == cost):
                return jsonify({"Your Choice":"Chocolate",  "Quantity": quantity})
            elif(amt>cost):
                blance = int(amt)-cost
                return jsonify({"Your Choice":"Chocolate", "Quantity": quantity, "Your Blance": blance})
            else:
                return jsonify({"message":"Insufficient Amount", "Take Back your money":amt})
    else:
        return jsonify({"This item is not available":item_name, "Take Back your money":amt})
