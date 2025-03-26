from flask import Flask, render_template
import requests

app = Flask(__name__)

API_kategorie = "https://www.themealdb.com/api/json/v1/1/categories.php"
API_posilki = "https://www.themealdb.com/api/json/v1/1/filter.php"
API_przepis = "https://www.themealdb.com/api/json/v1/1/lookup.php"


@app.route('/')
def index():
    response = requests.get(API_kategorie)

    if response.status_code == 200:
        data = response.json()
        categories = data.get("categories", [])
    else:
        categories = []

    return render_template('index.html', categories=categories)

@app.route('/kategoria<category_name>')
def category_meals(category_name):
    params = {"c": category_name}
    response = requests.get(API_posilki,params=params)
    if response.status_code == 200:
        data = response.json()
        meals= data.get("meals", [])
    else:
        meals=[]

    return render_template('kategoria.html',category_name=category_name, meals=meals)

@app.route('/meal<meal_id>')
def meals(meal_id):
    params = {"i": meal_id}
    response = requests.get(API_przepis,params=params)
    if response.status_code == 200:
        data = response.json()
        recipes=data.get("meals", [])[0]
    else:
        recipes=[]
    return render_template('przepis.html',meal_id=meal_id, recipes=recipes)


if __name__ == '__main__':
    app.run(debug=True)