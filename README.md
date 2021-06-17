# jinja
## Problem: Practicing Python Jinja and Flask
## Solutions
1. Get current year in the footer
```
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.today().year
    return render_template("index.html", num=random_number, CURRENT_YEAR=current_year)
    
...

<footer>
    <p>Copyright {{ CURRENT_YEAR }}. Built by ByoungJun Jo</p>
</footer>
```
2. Use API and render it using Jinja
```
@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get("https://api.genderize.io", {"name": name})
    gender = gender_response.json()['gender']
    age_response = requests.get("https://api.agify.io/", {"name": name})
    age = age_response.json()['age']
    return render_template("guess.html", name=name.title(), gender=gender, age=age)

...

<body>
    <h1>Hey {{ name }},</h1>
    <h2>I think you are {{ gender }}.</h2>
    <h3>And maybe {{ age }} years old.</h3>
</body>
```
3. Render blog posts using JSON and Jinja
```
@app.route('/blog')
def get_blog():
    blog_response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    blog_contents = blog_response.json()
    return render_template("blog.html", contents=blog_contents)

...

<body>
    {% for content in contents: %}
        {% if content['id'] == 2 %}
            <h1>{{ content['title'] }}</h1>
            <h3>{{ content['subtitle'] }}</h3>
        {% endif %}
    {% endfor %}
</body>
```
## Lessons
1. Read the documentations for Jinja and Flask
2. Make sure using {{ endif/for }} when you finish with the Python script in HTML
