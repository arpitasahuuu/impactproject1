from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load recipes from a JSON file
def load_recipes(filename='recipes.json'):
    try:
        with open(filename, 'r') as file:
            recipes = json.load(file)
            return recipes
    except FileNotFoundError:
        return []

# Save recipes to a JSON file
def save_recipes(recipes, filename='recipes.json'):
    with open(filename, 'w') as file:
        json.dump(recipes, file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_recipe():
    name = request.form['name']
    ingredients = request.form['ingredients'].split(',')
    instructions = request.form['instructions']
    
    recipes = load_recipes()
    recipes.append({
        'name': name,
        'ingredients': [ingredient.strip() for ingredient in ingredients],
        'instructions': instructions
    })
    save_recipes(recipes)
    
    return redirect(url_for('index'))

@app.route('/recipes')
def recipes():
    recipes = load_recipes()
    return render_template('recipes.html', recipes=recipes)

@app.route('/meal_plan')
def meal_plan():
    recipes = load_recipes()
    return render_template('meal_plan.html', recipes=recipes)



if __name__ == '__main__':
    app.run(debug=True)