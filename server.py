from flask import Flask, render_template
import random
from datetime import datetime
import requests

agify_url = "https://api.agify.io"
genderize_url = "https://api.genderize.io"

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_datetime = datetime.now()
    current_year = current_datetime.year
    return render_template("index.html",
                           num=random_number,
                           year=current_year)


@app.route('/guess/<username>')
def guess_age(username):
    agify_parameters = {
        'name': username
    }
    agify_response = requests.get(url=agify_url, params=agify_parameters)
    genderize_response = requests.get(url=genderize_url, params=agify_parameters)
    name = agify_response.json()['name']
    age = agify_response.json()['age']
    gender = genderize_response.json()['gender']

    return render_template("guess.html",
                           name=name,
                           age=age,
                           gender=gender
                           )


if __name__ == "__main__":
    app.run(debug=True)