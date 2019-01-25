from flask import Flask, render_template
from tinydb import TinyDB
# import os
import random
app = Flask(__name__)
db = TinyDB('db.json')
# I had set up the .env file but it doesnt make sense
# for this since db is not a hard path but relational.
# TINYDB_PATH = os.getenv('TINYDB_PATH')
# db = TinyDB(TINYDB_PATH)


@app.route('/')
def hello_world():
    recipes = db.all()
    recipe = random.choice(recipes)
    return render_template('recipe.html', recipe=recipe)
