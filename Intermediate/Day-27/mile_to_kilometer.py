import tkinter
from tkinter import *


def calculate_km():
    miles = float(miles_entry.get())
    km = str(round(miles * 1.6, 2))
    km_result_label.config(text=km)
    miles_entry.delete(0, END)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=600, width=300)
window.config(pady=15, padx=10)

miles_entry = Entry(width=15)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
