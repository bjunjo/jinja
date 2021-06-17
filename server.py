from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.today().year
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get("https://api.genderize.io", {"name": name})
    gender = gender_response.json()['gender']
    age_response = requests.get("https://api.agify.io/", {"name": name})
    age = age_response.json()['age']
    return render_template("guess.html", name=name.title(), gender=gender, age=age)

@app.route('/blog')
def get_blog():
    blog_response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    blog_contents = blog_response.json()
    return render_template("blog.html", contents=blog_contents)

if __name__ == "__main__":
    app.run(debug=True)