from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file(web_site, user_name, pwd):
    with open('data.txt', 'a') as f:
        f.write(f'{web_site} | {user_name} | {pwd}\n')


def reset_entry_field():
    entry_pwd.delete(0, END)
    entry_website.delete(0, END)
    entry_website.focus()


def btn_add_onclick():
    web_site = entry_website.get()
    user_name = entry_username.get()
    pwd = entry_pwd.get()
    save_file(web_site, user_name, pwd)
    reset_entry_field()


def btn_gen_pwd_onclick():
    print("click generate pwd")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.geometry("240x240")
# window.minsize(width=240, height=240)
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
img_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1, sticky="W")

# row 1
current_row = 1
lbl_website = Label(text="Website:")
lbl_website.grid(row=current_row, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=current_row, column=1, columnspan=2, sticky="W")
entry_website.focus()

current_row = 2
# row 2
lbl_username = Label(text="Email/Username:")
lbl_username.grid(row=current_row, column=0)
entry_username = Entry(width=35)
# entry_username.insert(-1, 'default text')
entry_username.insert(END, "test@test.com")
entry_username.grid(row=current_row, column=1, columnspan=2, sticky="W")

# row 3
current_row = 3
lbl_pwd = Label(text="Password:")
lbl_pwd.grid(row=current_row, column=0)
entry_pwd = Entry()
entry_pwd.grid(row=current_row, column=1)

btn_gen_pwd = Button(text="Generate Password", command=btn_gen_pwd_onclick)
btn_gen_pwd.grid(row=current_row, column=2, sticky="W")

# row 4
current_row = 4
btn_add = Button(text="Add", width=36, command=btn_add_onclick)
btn_add.grid(row=current_row, column=1, columnspan=2, sticky="W")

window.mainloop()
