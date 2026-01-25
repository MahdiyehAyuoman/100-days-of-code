from flask import Flask, render_template, url_for
import requests
import json


BLOG_URL = "https://api.npoint.io/ec4fe0f7af31a18d5f84"
response = requests.get(BLOG_URL)
posts = response.json()


web = Flask(__name__)
# @web.route('/')
# def home():
#     return render_template('index.html',posts=posts)

@web.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@web.route('/About')
def about():
    return render_template('about.html')



@web.route('/Contact')
def contact():
    return render_template('contact.html')

@web.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    web.run(debug=True)


