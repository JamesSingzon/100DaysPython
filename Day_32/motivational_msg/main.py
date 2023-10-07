import smtplib
import datetime as dt
from credentials import my_email, password
from random import choice

with open(file="Day_32/motivational_msg/quotes.txt") as quotes:
    quote = choice(quotes.readlines())
    print(f"\n{quote}\n")

MY_EMAIL = my_email
MY_PASSWORD = password
RECEIVER = "michellelarson13@gmail.com"

now = dt.datetime.now().day
print(now)


if now == 6:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user = MY_EMAIL, password = MY_PASSWORD)
                connection.sendmail(
                from_addr = MY_EMAIL, 
                to_addrs = RECEIVER, 
                msg = f"Subject:Weekend Quote!\n\n\n{quote}\n"
                )


# with open("Day_32/quotes.txt", mode="r") as file:
#     quote_list = [quote.strip() for quote in file.readlines()]

# print(f"\n{choice(quote_list)}\n")

# now = dt.datetime.now()

# print(now)

# with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        # connection.sendmail(
        #     from_addr = MY_EMAIL, 
        #     to_addr = "singzonseeds@yahoo.com",
        #     msg = f"Subject: Weekend motivation!\n\n{choice(quote_list)}"
        #     )

