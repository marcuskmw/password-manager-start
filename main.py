from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title ( "Password Manager")
# window.geometry("240x240")
# window.minsize(width=240, height=240)
window.config(padx = "20" ,pady="20")
canvas = Canvas(height = 200, width =200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=myimg)
canvas.pack()
window.mainloop()