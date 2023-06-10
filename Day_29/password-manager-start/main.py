from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ran_let = [password_list.append(choice(letters)) for _ in range(randint(8,10))]
    ran_num = [password_list.append(choice(numbers)) for _ in range(randint(2,4))]
    ran_sym = [password_list.append(choice(symbols)) for _ in range(randint(2,4))]

    password_list = ran_let + ran_num + ran_sym
    shuffle(password_list)
    password = "".join(set(password_list))

    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("Day_29/password-manager-start/data.txt",mode="a") as data:
                data.write(f"{website}\n{email}\n{password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
#GUI window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#Lock canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="Day_29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
#Website Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
#Email/Username Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "YouWannaKnow@gmail.com")

#Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
#Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
#Password Button
generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(column=2, row=3)

#Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()