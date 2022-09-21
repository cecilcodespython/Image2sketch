from cProfile import label
from lib2to3.pytree import convert
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("500x500")
root.title("image to sketch")
root.configure(bg='black')
root.resizable(False,False)



label1 =Label(root,text='IMG2SKETCH',fg='white',bg='black',font='Arial 30 bold').place(x=130,y=0)

first_frame =Frame(root,bd=3,width=200,height=200,relief=GROOVE,bg='#00A9A5')
first_frame.place(x=170,y=80)

first_label = Label(first_frame,bg='#00A9A5')
first_label.place(x=20,y=20)

def image_add():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
    title='Select Image File',
    filetypes=(('PNG File','*.png'),('Jpeg Files',"*jpg"),('All Files','*txt')))
    print(filename)
    img = Image.open(filename)
    img = ImageTk.PhotoImage(image=img)
    first_label.configure(image=img,width=150,height=150)
    first_label.image = img

def convert2image():
    image = cv2.imread(filename,0)
    grey = cv2.cvtColor(image,cv2.COLOR_BAYER_BG2GRAY)
    invert = cv2.bitwise_not(grey)
    blur=cv2.GaussianBlur(invert,(21,21),0)
    invertblur = cv2.bitwise_not(blur)

    sketch = cv2.divide(grey,invertblur,scale=256.0)
    cv2.imwrite('sketch.png',sketch)


add_image = Button(root,text="add_image",bg='white',fg='black',width=10,height=2,command=image_add).place(x=50,y=300)
to_sketch = Button(root,text="convert",bg='white',fg='black',width=10,height=2,command=convert2image).place(x=350,y=300)



root.mainloop()