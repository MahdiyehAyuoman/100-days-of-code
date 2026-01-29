
from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired,InputRequired, Email
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)



checked_email = "admin@email.com"
checked_password = "12345678"

def check_password_length(field, form):
    if len(field.data) > 8:
        raise ValidationError('Field must be at least 8 characters long')
    

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email("Invalid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(),InputRequired(), check_password_length])
    submit = SubmitField(label='Log In')

 
app.secret_key = "string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():  
    form = MyForm()
    email = form.email.data
    password = form.password.data
    form.validate_on_submit()
    if form.validate_on_submit():
        if email==checked_email and password==checked_password:
            # print("This is DONE!!!")
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template("login.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)
