##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random
import os
from pathlib import Path
import glob
import pathlib

# 1. Update the birthdays.csv 
birthday = pd.read_csv("birthdays.csv")

## Make a list of letter_templates, choise random of them
root_directory = r"letter_templates"
letter_templates_dir = pathlib.Path(root_directory)
txt_files_paths = list(letter_templates_dir.rglob('*.txt'))
letter_templates_dir_list = [str(path) for path in txt_files_paths]
random_letter = random.choice(letter_templates_dir_list)


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_year = today.year
today_month = today.month
today_day = today.day
# print(today_day)

# iterate over rows
for i, row in birthday.iterrows():
    birthday_month = row['month']
    birthday_day = row['day']
    birthday_person = row['name']
    # print(birthday_month)
    # print(birthday_day)

    if birthday_month == today_month and birthday_day == today_day:
        # print(f"{today_month}\n {today_day}")
        # print(row['name'])

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
        #  with the person's actual name from birthdays.csv
        search_text = '[NAME]'
        with open(random_letter, 'r') as file:
            random_letter = file.read()
            random_letter = random_letter.replace(search_text, birthday_person)
        # print(random_letter)

        # 4. Send the letter generated in step 3 to that person's email address.
        first_gmail = 'mahdiyehayuoman@gmail.com'
        gmail_password = 'write your password'
        second_mail = 'write your email'

        ## Send the quote of the day via email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=first_gmail, password=gmail_password)
            connection.sendmail(from_addr=first_gmail, 
                                to_addrs=second_mail, 
                                msg=(f"subject:Happy Birthday ;)\n\n{random_letter}"))
            connection.close()



