import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
    pass_entry.delete(0, END)
    password_list=[choice(letters) for l in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for n in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(string=password,index=END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website=website_entry.get()
    email=user_entry.get()
    password=pass_entry.get()
    new_data={website:{
        "email":email,
        "password":password
    }}
    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops",message="Dont leave plank fields check please!!")
    else:
        try:
            with open("data.json","r") as data_file:
                # Read the old data
                data =json.load(data_file)
                # updating the old data
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        website_entry.delete(0,END)
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
# ---------------------------- SEARCH METHOD ------------------------------- #
def find_password():
    text=website_entry.get()
    with open("data.json","r") as searched_file:
        data=json.load(searched_file)
        try:
            messagebox.showinfo(title=f"{text}",message=f"Email: {data[text]['email']} \n "
                                                        f"Password: {data[text]['password']}")
        except KeyError:
            messagebox.showinfo(title="Oops", message=f"No data matches the entered name:{text} ")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manger")
window.config(pady=20,padx=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Website elements
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1)

website_button=Button(text="Search", command=find_password,width=10)
website_button.grid(column=2,row=1)

# User elements
user_label=Label(text="Email/Username:")
user_label.grid(column=0,row=2)

user_entry=Entry(width=35)
user_entry.insert(string="example@outlook.com",index=END)
user_entry.grid(column=1,row=2,columnspan=2)

# Password elements
pass_label=Label(text="Password:")
pass_label.grid(column=0,row=3)

pass_entry=Entry(width=22)
pass_entry.grid(column=1,row=3)

pass_button=Button(text="Generate Password",command=generate_pass)
pass_button.grid(column=2,row=3)

# last Button
add_button=Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()