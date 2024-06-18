from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    # print(all_posts)
    return render_template("index.html", blogs=all_posts)

@app.route('/blog/<blog_id>')
def get_blog():
    return render_template("index.html", blogs=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
