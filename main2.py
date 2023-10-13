import tkinter as tk
import random

W, H = 1280, 720
num = 16
posX, posY = 0, 0

mouseX = 0
mouseY = 0

targetList = []


def mouseClick(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y
    targetDestroy()


def targetDestroy():
    global mouseX, mouseY
    count = 0
    for n in targetList:
        if (n.posX - n.size) <= mouseX <= (n.posX + n.size) and (
            n.posY - n.size
        ) <= mouseY <= (n.posY + n.size):
            print(f"TAG{count}")
            print(f"mouseX:{mouseX}")
            print(f"mouseY:{mouseY}")
            print(f"targetX-:{n.posX - n.size}")
            print(f"targetX+:{n.posX + n.size}")
            print(f"targetY-:{n.posY - n.size}")
            print(f"targetY+:{n.posY + n.size}")
            tar = targetList.pop(count)
            print(f"targetpositionX:{tar.posX}")
            print(f"targetpositionY:{tar.posY}")
            cvs.delete(f"TAG{count}")
            break
        else:
            count += 1


def createObj():
    global posX, posY, targetList
    countTag = 0
    cvs.delete("all")
    for n in range(1, 5, 1):
        for m in range(1, 5, 1):
            posX = int(random.randint(1, W / 4)) + ((W / 4) * (n - 1))
            posY = int(random.randint(1, H / 4)) + ((H / 4) * (m - 1))
            print(posX)
            print(posY)
            target = Target(posX, posY, 5, img)
            cvs.create_image(posX, posY, image=target.img, tag=f"TAG{countTag}")
            countTag += 1
            print(f"TAG{countTag}")
            targetList.append(target)


class Target:
    def __init__(self, posX=0, posY=0, size=0, img="img"):
        self.posX = posX
        self.posY = posY
        self.size = size
        self.img = img


root = tk.Tk()
root.geometry(f"{W}x{H}")
root.bind("<Button>", mouseClick)
cvs = tk.Canvas(root, width=W, height=H, bg="white")
img = tk.PhotoImage(file="Test2/obj5.png")
cvs.pack()

createObj()
root.mainloop()
