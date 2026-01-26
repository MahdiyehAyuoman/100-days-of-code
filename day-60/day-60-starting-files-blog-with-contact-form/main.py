from flask import Flask, render_template, request
import requests
import smtplib
import socks
import socket

# جایگزین کردن پورت واقعی سایفون به جای 51234
proxies = {
    "http": "http://127.0.0.1:50714",
    "https": "http://127.0.0.1:50714",
}

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/aac392a1f4baf5606b33", proxies=proxies).json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# 4. CHALLENGE
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        print(f'{name}\n{email} \n{phone_number} \n{message}')
        # return f"<h1>Successfully sent your message</h1>"

        # Step 6
        # send the user message to website owner's email
        first_gmail = 'mahdiyehayuoman@gmail.com'
        gmail_password = 'write your password'
        second_mail = 'write your email'
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=first_gmail, password=gmail_password)
            connection.sendmail(from_addr=first_gmail, 
                                to_addrs=second_mail, 
                                msg=(f"subject:New Message ;)\n\n Name: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"))
            connection.close()
    return render_template("contact.html")

## 3. CHALLENGE
# @app.route('/form_entry', methods=['POST', 'GET'])
# def recieve_data():
#     # if request.method == 'POST':
#     name = request.form['name']
#     email = request.form['email']
#     phone_number = request.form['phone']
#     message = request.form['message']
#     print(f'{name}\n{email} \n{phone_number} \n{message}')

#     return f"<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
