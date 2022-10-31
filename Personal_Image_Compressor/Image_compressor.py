
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

# This will return the the file path, store it in 'file_path'
file_path = askopenfilename()
#  Image.open() function to load an image, using a filepath
img = PIL.Image.open(file_path)

myHeight, myWidth = img.size  # storing the original image dimensions
# Returns a new object/image with the original dimensions, and compressed one
img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)

# this function is used to save a file in a specific location and store the path in variable 'save_path'
save_path = asksaveasfilename()
# saves the compressed image in the 'save_path' dir, with 'compressed.jpg' in the file name
img.save(save_path + "compressed.jpg")


window.mainloop
