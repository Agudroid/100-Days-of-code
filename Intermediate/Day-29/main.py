from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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

    is_ok = messagebox.askokcancel(title=web, message=f"These are the details: \n"
                                                      f"Email: {email}\n"
                                                      f"Password: {password}\n"
                                                      f"Do you want to save?")
    if is_ok:

        if web and password:
            with open('data.txt', mode='a') as file:
                file.write(web + ' | ' + email + ' | ' + password + '\n')
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title="Password Saved", message="The password was saved successfully")
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

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", padx=10, pady=10)
email_label.grid(row=2, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "agudonio@gmail.com")

password_label = Label(text="Password:", padx=10, pady=10)
password_label.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
