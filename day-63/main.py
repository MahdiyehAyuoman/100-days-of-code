from flask import Flask, app, render_template, request, redirect, url_for
# import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
all_books = []

@app.route('/')
def home():
    return render_template('index.html', all_books=db.session.query(Book).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    # if request.method == 'POST':
    #     new_book = {
    #         "title": request.form['title'],
    #         "author": request.form['author'],
    #         "rating": request.form['rating'],
    #     }

    title = request.form.get('title')
    author = request.form.get('author')
    rating = request.form.get('rating')
    if title != '' and author != '' and rating is not None:
        p = Book(title=title, author=author, rating=rating)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')
    

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.session.query(Book).filter_by(id=book_id).first()
    if request.method == "POST":
        new_rating = request.form.get('rating')
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)



@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)



