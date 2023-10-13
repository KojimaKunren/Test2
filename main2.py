import tkinter as tk
import random

W, H = 1280, 720
num = 16
posX, posY = 0, 0
mouseX, mouseY = 0, 0
targetList = []
targetInfoList = []
targetNumber = 1
targetNumberMax = 6


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
            cvs.delete(n.tag)
            targetList.pop(count)
            if len(targetList) <= 0:
                targetNumber += 1
                if targetNumber >= targetNumberMax:
                    targetNumber = 1
                createObj(targetNumber)
            break
        else:
            count += 1


def createObj(targetNumber):
    global posX, posY, targetList, targetInfoList, targetNumberMax
    countTag = 0
    cvs.delete("all")
    currentTarget = targetInfoList[targetNumber]
    if currentTarget.num == 1:
        target = Target(W / 2, H / 2, currentTarget.size, img1, tag="TAG0")
        targetList.append(target)
    elif currentTarget.num == 2:
        for n in range(1, currentTarget.num, 1):
            for m in range(1, currentTarget.num, 1):
                posX = int(random.randint(1, W / 2)) + ((W / 2) * (n - 1))
                posY = int(random.randint(1, H)) + (H * (m - 1))
                target = Target(
                    posX, posY, currentTarget.size, img2, tag=f"TAG{countTag}"
                )
                cvs.create_image(posX, posY, image=target.img, tag=f"TAG{countTag}")
                countTag += 1
                targetList.append(target)
    elif 2 < currentTarget.num < targetNumberMax:
        for n in range(1, currentTarget.num / 2, 1):
            for m in range(1, currentTarget.num / 2, 1):
                posX = int(random.randint(1, W / (currentTarget.num / 2))) + (
                    (W / (currentTarget.num / 2)) * (n - 1)
                )
                posY = int(random.randint(1, H / (currentTarget.num / 2))) + (
                    (H / (currentTarget.num / 2)) * (m - 1)
                )
                target = Target(
                    posX,
                    posY,
                    currentTarget.size,
                    currentTarget.img,
                    tag=f"TAG{countTag}",
                )
                cvs.create_image(
                    posX, posY, image=currentTarget.img, tag=f"TAG{countTag}"
                )
                countTag += 1
                targetList.append(target)


class Target:
    def __init__(self, posX=0, posY=0, size=0, img="img", tag="tag"):
        self.posX = posX
        self.posY = posY
        self.size = size
        self.img = img
        self.tag = tag


class TargetInfo:
    def __init__(self, name="name", num=0, size=0, img="img"):
        self.name = name
        self.num = num
        self.size = size
        self.img = img


root = tk.Tk()
root.geometry(f"{W}x{H}")
root.bind("<Button>", mouseClick)
cvs = tk.Canvas(root, width=W, height=H, bg="white")
img1 = tk.PhotoImage(file="Test2/image/obj1.png")
img2 = tk.PhotoImage(file="Test2/image/obj2.png")
img3 = tk.PhotoImage(file="Test2/image/obj3.png")
img4 = tk.PhotoImage(file="Test2/image/obj4.png")
img5 = tk.PhotoImage(file="Test2/image/obj5.png")

target1 = TargetInfo("target1", 1, 400, img=img1)
target2 = TargetInfo("target2", 2, 300, img=img2)
target3 = TargetInfo("target3", 4, 150, img=img3)
target4 = TargetInfo("target4", 8, 80, img=img4)
target5 = TargetInfo("target5", 16, 20, img=img5)
targetInfoList = [target1, target2, target3, target4, target5]

cvs.pack()

createObj(targetNumber)
root.mainloop()
