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
@app.route('/meals')
def get_meals():
    return render_template("meals.html", meals=mongo.db.meals.find())

@app.route('/meal/view/<meal_id>')
def view_meal(meal_id):
    the_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    all_categories = mongo.db.categories.find()
    return render_template('viewmeal.html', meal=the_meal, categories=all_categories)

@app.route('/meal/add')
def add_meals():
    return render_template("addmeal.html",
    categories=mongo.db.categories.find())

@app.route('/meal/insert', methods=['POST'])
def insert_meal():
    meals = mongo.db.meals
    meals.insert_one(request.form.to_dict())
    return redirect(url_for('get_meals'))

@app.route('/meal/edit/<meal_id>')
def edit_meal(meal_id):
    the_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editmeal.html', meal=the_meal, categories=all_categories)

@app.route('/meal/copy/<meal_id>')
def copy_meal(meal_id):
    the_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    all_categories = mongo.db.categories.find()
    return render_template('copymeal.html', meal=the_meal, categories=all_categories)



@app.route('/meal/update/<meal_id>', methods=["POST"])
def update_meal(meal_id):
    meals = mongo.db.meals
    meals.update(  {'_id': ObjectId(meal_id)},
    {
        'meal_name':request.form.get['meal_name'],
        'category_name':request.form.get['category_name'],
        'meal_description':request.form.get['meal_description'],
        'meal_time':request.form.get['meal_time'],
        'meal_ingredients':request.form.get['meal_ingredients'],
        'meal_instructions':request.form.get['meal_instructions'],
        'meal_tips':request.form.get['meal_tips'],
        'meal_temp':request.form.get['meal_temp']
    })
    return redirect(url_for('get_meals'))

@app.route('/meal/delete/<meal_id>')
def delete_confirm(meal_id):
    the_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    all_categories = mongo.db.categories.find()
    return render_template('delete.html', meal=the_meal, categories=all_categories)

@app.route('/delete_meal/<meal_id>')
def delete_meal(meal_id):
    mongo.db.meals.remove({'_id': ObjectId(meal_id)})
    return redirect(url_for('get_meals'))

@app.route('/filter/indian')
def sort_by_indian():
    return render_template('indian.html', meals=mongo.db.meals.find())

@app.route('/filter/american')
def sort_by_american():
    return render_template('american.html', meals=mongo.db.meals.find())

@app.route('/filter/asian')
def sort_by_asian():
    return render_template('asian.html', meals=mongo.db.meals.find())

@app.route('/filter/british')
def sort_by_british():
    return render_template('british.html', meals=mongo.db.meals.find())

@app.route('/filter/italian')
def sort_by_italian():
    return render_template('italian.html', meals=mongo.db.meals.find())

@app.route('/filter/desserts')
def sort_by_desserts():
    return render_template('desserts.html', meals=mongo.db.meals.find())

@app.route('/filter/middle-eastern')
def sort_by_middle_eastern():
    return render_template('middle-eastern.html', meals=mongo.db.meals.find())

@app.route('/filter/french')
def sort_by_french():
    return render_template('french.html', meals=mongo.db.meals.find())

@app.route('/filter/african')
def sort_by_african():
    return render_template('african.html', meals=mongo.db.meals.find())

@app.route('/filter/other')
def sort_by_other():
    return render_template('other.html', meals=mongo.db.meals.find())

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
