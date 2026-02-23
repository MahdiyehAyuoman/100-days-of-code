from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from requests import post, request
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, form
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# WTForm
class PostForm(FlaskForm):
    blog_title = StringField('Blog post title', validators=[DataRequired()])
    blog_subtitle = StringField('Subtitle', validators=[DataRequired()])
    author_name = StringField('Your name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog content') 
    
    submit = SubmitField('Submit')


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.  Done

    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars()
    return render_template("index.html", all_posts=posts)



# TODO: Add a route so that you can click on individual posts.  Done
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id  Done
    requested_post = db.session.get(BlogPost, post_id)
    # requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.blog_title.data,
            subtitle = form.blog_subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            body = form.body.data,
            author = form.author_name.data,
            img_url = form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(
        blog_title = post_to_edit.title,
        blog_subtitle = post_to_edit.subtitle,
        author_name = post_to_edit.author,
        img_url = post_to_edit.img_url,
        body = post_to_edit.body
    )
    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.blog_title.data
        post_to_edit.subtitle = edit_form.blog_subtitle.data
        post_to_edit.author = edit_form.author_name.data
        post_to_edit.img_url = edit_form.img_url.data
        post_to_edit.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete-post/<int:post_id>', methods=["GET", "POST"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars()
    return render_template("index.html", all_posts=posts)
    
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

