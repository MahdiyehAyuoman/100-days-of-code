from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_blogs = response.json()
    return render_template("index.html",  blogs=all_blogs)


@app.route("/post/<num>")
def get_blog(num):
    print(num)
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_blogs = response.json()
    return render_template(f"post{num}.html",  blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)


#  URL/post/blog_id