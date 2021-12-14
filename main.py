import smtplib
import os
from dotenv import load_dotenv

# loading .env file
load_dotenv()

# accessing variables stored in .env
my_email = os.environ.get("my-email")
password = os.environ.get("password")
recipient = os.environ.get("recipient")

my_email = "riccardofeingold@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection: # connection to the mail server
    connection.starttls() # this makes the connection to the mail server secure
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg="Subject:HELLO!\n\nThis is the body of my email."
    )
