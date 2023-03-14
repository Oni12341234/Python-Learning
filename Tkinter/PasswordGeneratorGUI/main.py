# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ------------------------- --- SAVE PASSWORD ------------------------------- #

def add_input():
    global website_entry, email_entry, password_entry
    website= website_entry.get()
    email= email_entry.get()
    password= password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }
    if len(password)==0 or len(website)==0:
        messagebox.showinfo(title="Invalid input", message="You left an entry empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detailes enterd: \nEmail: {email} \nPassword: {password}\n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data= json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else: 
                with open("data.json", "r") as file:
                    data = json.load(file)
                with open("data.json", "w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            finally:           
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
            messagebox.showinfo(title="Saved", message="Your password has been saved")


def search():
    website_search=website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not found", message="There is no data to be found")
    else:
        if website_search in data:
            messagebox.showinfo(title = website_search, message=f"E-mail: {data[website_search]['email']}\n Password : {data[website_search]['password']}")
        else:
            messagebox.showinfo(title = "Not found", message= f"There is no data for website {website_search}")
# ---------------------------- UI SETUP ------------------------------- #
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

window = tkinter.Tk()
window.title("GUI Password Manager")
window.config(padx=50, pady=50)



canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=1)



website_label = tkinter.Label(text="Website:", font=("Courier", 10, "normal"))
website_label.grid(column=0, row=4)

email_label = tkinter.Label(text="Email/Username:", font=("Courier", 10, "normal"))
email_label.grid(column=0, row=5)

password_label = tkinter.Label(text="Password:", font=("Courier", 10, "normal"))
password_label.grid(column=0, row=6)

website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=4 , columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "oni@email.ro")
email_entry.grid(column=1, row=5 ,columnspan=2)

password_entry= tkinter.Entry(width=21)
password_entry.grid(column=1, row=6 , columnspan=2)

generate_button = tkinter.Button(command=generate_password)
generate_button["text"] = "Generate password"
generate_button.grid(column = 2, row = 6)

add_button = tkinter.Button(width=36, command=add_input)
add_button["text"] = "Add"
add_button.grid(column = 1, row = 7, rowspan=2)

search_button = tkinter.Button(width = 15,command=search)
search_button["text"]= "Search"
search_button.grid(column=2 , row=4)

window.mainloop()