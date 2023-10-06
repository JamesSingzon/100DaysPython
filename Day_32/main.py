import smtplib
from credentials import my_email, password



sender_email = my_email
sender_password = password

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=sender_email,password=sender_password)
connection.sendmail(from_addr=sender_email, to_addrs="singzonseeds@yahoo.com", msg="Hello")
connection.close()