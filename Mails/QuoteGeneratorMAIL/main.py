import datetime as dt
import random 

now = dt.datetime.now()
now_day = now.weekday()
with open("quotes.txt") as file:
    content = file.readlines()
    quote = random.choice(content)
print(now_day)
if now_day==2:
        import smtplib
        my_email = "idobre2307@gmail.com"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password="sfnwsyrrmomkkpyk" )
        connection.sendmail(from_addr=my_email, to_addrs="idobre0608@gmail.com", msg=f"Subject:Hello\n\n{quote}")
        connection.close()
