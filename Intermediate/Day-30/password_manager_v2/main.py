from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD  ------------------------------- #


def search_website():
    web = website_entry.get()
    with open('data.json', mode='r') as file:
        data = json.load(file)
    try:
        password = data[web]['password']
    except KeyError as key_error_msg:
        messagebox.showwarning(title='Password Manager', message=f'Website {key_error_msg} not found')
    else:
        messagebox.showinfo('Password Manager', message=f'The password for the web {web}\n'
                                                        f'is: {password}')
        pyperclip.copy(password)
    finally:
        website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd',
               'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p',
               'q', 'r', 's', 't',
               'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters-1)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers - 1)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols - 1)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        web: {
            'email': email,
            'password': password
        }
    }
    if web and password:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo(title="Password Saved", message="The password was saved successfully")
        pyperclip.copy(password)
    else:
        messagebox.showwarning(title="Empty Information", message="Please, fill or fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text='Search', width=15, command=search_website)
search_button.grid(row=1, column=2, columnspan=2)

email_label = Label(text="Email/Username:", padx=15, pady=10)
email_label.grid(row=2, column=0)

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, padx=28)
email_entry.insert(0, "agudonio@gmail.com")

password_label = Label(text="Password:", padx=10, pady=10)
password_label.grid(row=3, column=0)

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=password_generator, width=15)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
