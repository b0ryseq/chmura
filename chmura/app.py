from flask import Flask, render_template
import requests

app = Flask(__name__)

API_CATEGORIES = "https://www.themealdb.com/api/json/v1/1/categories.php"
API_MEALS = "https://www.themealdb.com/api/json/v1/1/filter.php"
API_RECIPE = "https://www.themealdb.com/api/json/v1/1/lookup.php"

@app.route('/')
def index():
    response = requests.get(API_CATEGORIES)
    categories = response.json().get("categories", []) if response.status_code == 200 else []
    return render_template('index.html', categories=categories)

@app.route('/category/<category_name>')
def category_meals(category_name):
    response = requests.get(API_MEALS, params={"c": category_name})
    meals = response.json().get("meals", []) if response.status_code == 200 else []
    return render_template('kategoria.html', category_name=category_name, meals=meals)

@app.route('/meal/<meal_id>')
def meals(meal_id):
    response = requests.get(API_RECIPE, params={"i": meal_id})
    meals_data = response.json().get("meals", []) if response.status_code == 200 else []
    recipe = meals_data[0] if meals_data else {}
    return render_template('przepis.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
