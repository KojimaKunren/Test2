import tkinter as tk
import time


def moveRight():
    cvs.move("cvs1",0.1,0)
    cvs.after(50,moveLeft)

def moveLeft():
    cvs.move("cvs1",-0.1,0)
    cvs.after(50,moveRight)

def shake():
    for _ in range(5):
        moveRight()

root=tk.Tk()
root.geometry("1280x720")
img=tk.PhotoImage(file="Test2/image/obj4.png")
cvs=tk.Canvas(root,width=1280,height=720)
cvs.create_image(640,360,image=img,tag="cvs1")
cvs.pack()

root.after(2000,shake)
root.mainloop()