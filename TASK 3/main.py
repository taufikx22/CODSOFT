from tkinter import *
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(letters_entry.get())
    nr_symbols = int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())

    final_password = ""
    for _ in range(nr_letters):
        final_password += random.choice(letters)
    for _ in range(nr_symbols):
        final_password += random.choice(symbols)
    for _ in range(nr_numbers):
        final_password += random.choice(numbers)

    final_password_list = list(final_password)
    random.shuffle(final_password_list)
    final_password_shuffled = ''.join(final_password_list)

    password_label.config(text=final_password_shuffled)
    pyperclip.copy(final_password_shuffled)

window = Tk()
window.title("Password Generator")

font_style = ('Arial', 12)

letters_label = Label(window, text="Number of letters:", font=font_style)
letters_label.grid(row=0, column=0, sticky="nsew")
letters_entry = Entry(window, font=font_style)
letters_entry.grid(row=0, column=1, sticky="nsew")

symbols_label = Label(window, text="Number of symbols:", font=font_style)
symbols_label.grid(row=1, column=0, sticky="nsew")
symbols_entry = Entry(window, font=font_style)
symbols_entry.grid(row=1, column=1, sticky="nsew")

numbers_label = Label(window, text="Number of numbers:", font=font_style)
numbers_label.grid(row=2, column=0, sticky="nsew")
numbers_entry = Entry(window, font=font_style)
numbers_entry.grid(row=2, column=1, sticky="nsew")

generate_button = Button(window, text="Generate Password", command=generate_password, font=font_style)
generate_button.grid(row=3, column=0, columnspan=2, sticky="nsew")

password_label = Label(window, text="", font=('Arial', 14, 'bold'))
password_label.grid(row=4, column=0, columnspan=2, sticky="nsew")

for i in range(5):
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()
