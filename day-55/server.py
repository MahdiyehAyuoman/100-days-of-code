from flask import Flask
import random

new = Flask(__name__)

random_number = random.randint(0,9)
print(f"random_number: {random_number}")
@new.route("/")
def hello():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src ='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2Zpa2E0a2d0MWptM3N2YzhqNnhvOHY5a3R4Yjl3eGFndm91enprZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@new.route("/<int:number>")
def what_number(number):
    if number < random_number:
        return too_low()
    elif number > random_number:
        return too_high()
    else:
        return correct()
    
def too_low():
    return "<h1 style='color: red'>is too low:</h1>"\
        "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

def too_high():
    return "<h1 style='color: purple'>is too high:</h1>"\
        "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


def correct():
    return "<h1 style='color: green'>is just right:</h1>"\
        "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"



if __name__ == "__main__":
    new.run(debug=True)













