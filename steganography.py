from tkinter import *
from tkinter import filedialog,messagebox as mb
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import os
import cv2
from bitstring import BitArray as ba


root = Tk()
root.title("My App")
root.geometry("700x500+250+50")
root.resizable(False,False)
root.configure(bg= "#3b3d3c")


def showimage1():
    global filename,img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Choose an Image to Display",
                                          filetypes=(("JPG file","*.jpg"),
                                                     ("PNG file","*.png")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl_disp_img_frame.configure(image = img , width=275,height=270)
    lbl_disp_img_frame.image = img
def showimage2():
    global filename2,img2
    filename2 = filedialog.askopenfilename(initialdir=os.getcwd(),title="Choose an Image to Display",
                                          filetypes=(("JPG file","*.jpg"),
                                                     ("PNG file","*.png")))
    img2 = Image.open(filename2)
    img2 = ImageTk.PhotoImage(img2)
    lbl_hide_img_frame.configure(image = img2 , width=275,height=270)
    lbl_hide_img_frame.image = img2
def save(img):
    data = Image.fromarray(img)
    data.save("hidden.png")
    mb.showinfo("Successfully","Image Hide Successfully")
def hide():
    image1 = cv2.imread(filename)
    image2 = cv2.imread(filename2)
    if image1.shape == image2.shape:
        image1 = (image1 & 0b11110000)
        image2 = (image2 & 0b11110000)
        
        image3 = image1+(image2 >> 4)
        save(image3)

    else:
        mb.showerror("Unequal Image size","both images must have same resolutions")
        mb.showinfo("Image Size",f"Image size of display image is {image1.shape[0]} x {image1.shape[1]}")
        mb.showinfo("Image Size",f"Image size of display image is {image2.shape[0]} x {image2.shape[1]}")
def show():
    image1 = cv2.imread("hidden.png")
    image2 = np.zeros(shape=[image1.shape[0], image1.shape[1], 3])
    d = (image1 & 0b00001111) 
    image2 = d << 4
    cv2.imshow("Recovered Image",image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



Label(root,text="Steganography",bg="#3b3d3c",fg="white",font="Sans 28 bold").place(x=210,y=20)

display_Image_Frame = Frame(root, bd=3,bg="black",width=320,height=280,relief=GROOVE)
display_Image_Frame.place(x=20,y=90)

lbl_disp_img_frame = Label(display_Image_Frame,bg="black")
lbl_disp_img_frame.place(x=20,y=10)

hide_Image_Frame = Frame(root, bd=3,bg="black",width=320,height=280,relief=GROOVE)
hide_Image_Frame.place(x=360,y=90)

lbl_hide_img_frame = Label(hide_Image_Frame,bg="black")
lbl_hide_img_frame.place(x=20,y=10)

disp_btns_Frame = Frame(root, bd=3,bg="#3b3d3c",width=320,height=100,relief=GROOVE)
disp_btns_Frame.place(x=20,y=380)
Label(disp_btns_Frame,text="Upload an Image to Display",bg="#3b3d3c",fg="cyan",font="sans 9 bold").place(x=70,y=5)
Button(disp_btns_Frame,text="Upload Image",width=13,height=2,font="sans 12 bold",command=showimage1).place(x=10,y=30)
Button(disp_btns_Frame,text="Save Image",width=13,height=2,font="sans 12 bold",command=save).place(x=170,y=30)

hide_btns_Frame = Frame(root, bd=3,bg="#3b3d3c",width=320,height=100,relief=GROOVE)
hide_btns_Frame.place(x=360,y=380)
Label(hide_btns_Frame,text="Upload an Image to Hide",bg="#3b3d3c",fg="cyan",font="sans 9 bold").place(x=70,y=5)
Button(hide_btns_Frame,text="Upload",width=8,height=2,font="sans 12 bold",command=showimage2).place(x=10,y=30)
Button(hide_btns_Frame,text="Hide",width=8,height=2,font="sans 12 bold",command=hide).place(x=115,y=30)
Button(hide_btns_Frame,text="Show",width=8,height=2,font="sans 12 bold",command=show).place(x=220,y=30)




root.mainloop()
