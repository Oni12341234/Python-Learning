##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

import pandas
import datetime
import random
import smtplib
date_today = datetime.datetime.now()
contents = pandas.read_csv("birthdays.csv")
list_years = contents["year"].tolist()
list_months = contents["month"].tolist()
for index, row in contents.iterrows():
    if int(row["month"])==int(date_today.month):
        if int(row["day"])==int(date_today.day):
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file :
                letter_contents = file.read()
                print(letter_contents)
            x = letter_contents.replace("[NAME]", f"{row['name']}" )
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login("idobre2307@gmail.com", "btkmrauzxfwkozog")

            connection.sendmail("idobre2307@gmail.com", "idobre2307@gmail.com", f"Subject:Happy Birthday\n\n{x}")
            print("Message sent")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




