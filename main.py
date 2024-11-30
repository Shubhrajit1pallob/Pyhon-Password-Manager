from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    password_txt = password_entry.get()
    username_email_txt = username_email_entry.get()
    website_txt = website_entry.get()
    new_dict = {
        website_txt: {
            "email": username_email_txt,
            "password": password_txt
        }
    }

    if len(password_txt) < 1 or len(website_txt) < 1:
        messagebox.showerror(title="Oops", message="Please don't leave any feilds empty!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_dict, data_file, indent=2)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            data.update(new_dict)

            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=2)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- search details ------------------------------- #

def find_password():
    text = website_entry.get()
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File does not exists")
    else:
        if text in data:
            email_txt = data[text]["email"]
            pass_txt = data[text]["password"]
            final_txt = f"Email: {email_txt} \n Password: {pass_txt}"
            messagebox.showinfo(title=text, message=final_txt)
        else:
            messagebox.showerror(title="Error", message="No detail for the website exists")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

search_btn = Button(text="Search", command=find_password, width=11)
search_btn.grid(column=2, row=1)

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_email_label = Label(text="Email/Username:")
username_email_label.grid(column=0, row=2)

username_email_entry = Entry(width=36)
username_email_entry.insert(0, "shubhrajitpallob@gmail.com")
username_email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_pass_btn = Button(text="Generate Password", width=11, command=generate_password)
generate_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=34, command=add)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
