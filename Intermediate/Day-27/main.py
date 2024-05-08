from tkinter import *


def button_clicked():
    button_text = entry.get()
    if not button_text:
        my_label.config(text="Empty")
    else:
        my_label.config(text=button_text)


window = Tk()
window.title("My first Tkinter GUI Interface")
window.minsize(width=600, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Example Label", font=("Courier", 24, "bold"))
my_label["text"] = "new text"
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=20)

# Button
button_2 = Button(text="Click me 2", command=button_clicked)
button_2.grid(column=2, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
