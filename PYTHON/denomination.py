from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Window
root = Tk()
root.title('Denomination Counter')
root.configure( bg='light blue')
root.geometry9=('650x400')

# Adding Image and Labels in the main window
upload = Image.open("app_img.jpg")
# Resize the image using resize()method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
            text="Hey User! Welcome to Denomination Counter Application.",
            bg='light blue'  )
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function for opening new/top window
def topwin():
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50=50")


    LABEL = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are the number of notes for each denomination", bg='light grey')


    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount