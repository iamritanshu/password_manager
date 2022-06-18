import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

GOLD = "#1C364D"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    new_data = {website_entry.get(): {
        "email": email_entry.get(),
        "password": password_entry.get(),
    }}
    if (len(website_entry.get()) == 0) or (len(password_entry.get()) == 0):
        messagebox.showwarning(title="Oops..🙁", message="You have left any field empty")
    else:
        # --------- SAVING AS FILE MODE --------- #

        # is_okay = messagebox.askokcancel(title=website_entry.get(),
        #                                  message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\nAre your sure?")
        # if is_okay:
        # with open("data.txt", "a") as f:
        #     f.write(f"[{website_entry.get()}] | [{email_entry.get()}] | [{password_entry.get()}]\n")

        # --------- SAVING AS FILE MODE --------- #
        is_okay = messagebox.askokcancel(title=website_entry.get(),
                                         message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\nAre your sure?")
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)  # Reading data
                    data.update(new_data)  # Updating old data with new data
            except (FileNotFoundError, json.JSONDecodeError):
                data = new_data
            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Hurray!!🥳", message="Added successfully.")


# ---------------------------- SEARCH WEBSITE DATA ------------------------------- #
def search_data():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning(title="Error", message="No data file found.")
    else:
        if website_entry.get() in data:
            email = data[website_entry.get()]['email']
            password = data[website_entry.get()]['password']
            messagebox.showinfo(title=website_entry.get(),
                                message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No data for {website_entry.get()} was found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("|>@$$w()rd M@n@ger")
window.config(padx=50, pady=50, bg=GOLD)
window.resizable(0,0)  # It stops window to get minimize or maximize
canvas = Canvas(width=200, height=200, bg=GOLD, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", bg=GOLD, fg="white").grid(row=1, column=0)
website_entry = Entry(width=33, bg=GOLD, fg="white")
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

search_website_btn = Button(text="Search", bg="white", width=13, command=search_data)
search_website_btn.grid(row=1, column=2)

email_label = Label(text="Email/Username: ", bg=GOLD, fg="white").grid(row=2, column=0)
email_entry = Entry(width=52, bg=GOLD, fg="white")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "amr@email.com")

password_label = Label(text="Password: ", bg=GOLD, fg="white").grid(row=3, column=0)
password_entry = Entry(width=33, bg=GOLD, fg="white")
password_entry.grid(row=3, column=1)

generate_password_btn = Button(text="Generate Password", bg="white", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=44, bg="white", command=save_file)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
