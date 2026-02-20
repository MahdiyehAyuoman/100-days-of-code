from ast import stmt
from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from requests import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods = ["GET"])
def get_random_cafe():
    if request.method == "GET":
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(cafes)
        return jsonify(cafes={
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
            "has_sockets": random_cafe.has_sockets,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "id": random_cafe.id,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "name": random_cafe.name,
            "seats": random_cafe.seats,
            "map_url": random_cafe.map_url
        })
    


# HTTP GET - Read Record
@app.route("/all", methods = ['GET'])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])

@app.route('/search', methods = ['GET'])
def get_same_loc():
    location = request.args.get("loc")
    cafes = select(Cafe).where(Cafe.location == location)
    results = db.session.execute(cafes).scalars().all()
    ### if the input location does not exist in the database, return an error message.
    return jsonify(cafes=[cafe.to_dict() for cafe in results]) if results else jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})



# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200



# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    else:
        cafe = db.get(Cafe, cafe_id)
        if cafe is None:
            return jsonify(error={"Not Found": "Sorry, we couldn't find a cafe with that id."}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200

if __name__ == '__main__':
    app.run(debug=True)
