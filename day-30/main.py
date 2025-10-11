from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
import json

FONT = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list_letters = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    password_list_symbols = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    password_list_numbers = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_var.get()
    email = email_var.get()
    password = password_var.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    ## Check if user don't input any data
    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        data = "data.json"
        try:
            with open("data.json", "r") as pass_data:
                data = json.load(pass_data)

        except (FileNotFoundError, json.JSONDecodeError):
            data = new_data
        
        else:
            data.update(new_data)

        finally:
            with open("data.json", "w") as pass_data:
                json.dump(data, pass_data, indent=4)
                ## Clear the entries after add to file text
            website_entry.delete(0, END)
            password_entry.delete(0, END) 


# ---------------------------- FIND PASSWORD & WEBSITE ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as pass_data:
                data = json.load(pass_data)

        website = website_var.get()
        # email = email_var.get()
        # password = password_var.get()
        if website in data.keys():
            # print(f"{website} is in data.json")
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="NO details for the website exists")

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="NO Data File Found.")
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image =logo_image)
canvas.grid(row=0, column=1)


## Website 
website_title = Label(text='Website:', font=(FONT, 10))
website_title.grid(row=1, column=0)

## website Entry 
website_var = StringVar()
website_entry = Entry(width=35, textvariable = website_var)
website_entry.grid(row=1, column=1)
website_entry.focus()

## Search button 
search_button = Button(text='Search', width = 13, font=(FONT, 10), command=find_password)
search_button.grid(row=1, column=2)

## Email 
emial_title = Label(text='Emial/Username:', font=(FONT, 10))
emial_title.grid(row=2, column=0)

## Email Entry 
email_var = StringVar()
email_entry = Entry(width=35, textvariable = email_var)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'mahdiyehayuoman@gmail.com')

## Password 
password_title = Label(text='Password:', font=(FONT, 10))
password_title.grid(row=3, column=0)

## Password Entry 
password_var = StringVar()
password_entry = Entry(width=21, textvariable = password_var)
password_entry.grid(row=3, column=1)
password_button = Button(text='Generate Password', highlightthickness=0, font=(FONT, 10), command=password_generator)
password_button.grid(row=3, column=2)


## Add button
add_button = Button(text='Add', highlightthickness=0, font=(FONT, 10), width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()