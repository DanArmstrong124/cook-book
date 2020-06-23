import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Link the database into PyMongo

app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_meals')
def get_meals():
    return render_template("meals.html", meals=mongo.db.meals.find())

@app.route('/add_meals')
def add_meals():
    return render_template("addmeal.html",
    categories=mongo.db.categories.find())

@app.route('/insert_meal', methods=['POST'])
def insert_meal():
    meals = mongo.db.meals
    meals.insert_one(request.form)




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
