import tkinter as tk

mouseX = 0
mouseY = 0
objectX = 640
objectY = 360


def mouseClick(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y
    targetDestroy()


def targetDestroy():
    global mouseX, mouseY, objectX, objectY
    if 440 <= mouseX <= 840 and 160 <= mouseY <= 560:
        cvs.delete("TAG")
        cvs.create_image(objectX, objectY, image=img2, tag="TAG")


def main():
    global mouse_c
    cvs.delete("all")
    cvs.create_image(640, 360, image=img, tag="TAG")


root = tk.Tk()
root.title("Go")
root.geometry("1280x720")
root.bind("<Button>", mouseClick)
cvs = tk.Canvas(root, width=1280, height=720, bg="yellow")
img = tk.PhotoImage(file="Test2/obj1.png")
img2 = tk.PhotoImage(file="Test2/obj2.png")
cvs.pack()

main()
root.mainloop()
