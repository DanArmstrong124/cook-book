import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

#Link the database into PyMongo
mongo_db_name = os.environ.get('MNGDB_NAME')
mongo_db_pass = os.environ.get('MNGDB_PASS')

app.config["MONGO_DBNAME"] = mongo_db_name
app.config["MONGO_URI"] = mongo_db_pass

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_meals')
def get_meals():
    return render_template("meals.html", meals=mongo.db.meals.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)