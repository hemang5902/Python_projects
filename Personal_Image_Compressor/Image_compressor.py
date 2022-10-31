
import tkinter
from typing import Text
import PIL
from PIL import Image
from tkinter.filedialog import *

window = tkinter.Tk()
window.title("Image Compressor")
window.geometry('600x400')
# Function to compress the image

label = tkinter.Label(
    window, text="Compress your file here", font=("Arial Bold", 26)).pack()
label1 = tkinter.Label(
    window, text="Choose the file, then click Open", font=("Arial Bold", 26)).pack()
label2 = tkinter.Label(
    window, text="Now save the file with new name ", font=("Arial Bold", 26)).pack()
label3 = tkinter.Label(
    window, text="WOOSH..! Done ", font=("Arial Bold", 26)).pack()

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidht = img.size

img = img.resize((myHeight, myWidht), PIL.Image.ANTIALIAS)

save_path = asksaveasfilename()
img.save(save_path + "compressed.jpg")


window.mainloop
