from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Text Message")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2f4155")


def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(
        ("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=250, height=250)
    lb1.image = img


def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def save():
    secret.save("hidden.png")


# ICON
image_icon = PhotoImage(file="Stenograph_app\icons8.png")
root.iconphoto(False, image_icon)


# logo
logo = PhotoImage(file="Stenograph_app\spy_bhau.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="Cyber Secure", bg="#2d4155",
      fg="white", font="arial 25 bold").place(x=10, y=20)

# firstframe
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

# Second frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 20", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

Scrollbar1 = Scrollbar(frame2)
Scrollbar1.place(x=320, y=300)

Scrollbar1.config(command=text1.yview)
text1.config(yscrollcommand=Scrollbar1.set)

# third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2,
       font="arial 14 bold", command=showimage).place(x=20, y=30)

Button(frame3, text="Save Image", width=10, height=2,
       font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File",
      bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2,
       font="arial 14 bold", command=Hide).place(x=20, y=30)

Button(frame4, text="Show Data", width=10, height=2,
       font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File",
      bg="#2f4155", fg="yellow").place(x=20, y=5)


root.mainloop()
