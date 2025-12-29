from flask import Flask, render_template

web = Flask(__name__)

@web.route("/")
def home():
    # return render_template("Angela.html")
    return render_template("index.html")




if __name__ == "__main__":
    web.run(debug=True)

