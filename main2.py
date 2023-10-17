import tkinter as tk
import random
import time

W, H = 1280, 720
num = 16
posX, posY = 0, 0
mouseX, mouseY = 0, 0
score, timer = 0, 180
targetList = []
targetInfoList = []
targetShakeList = []
targetNumber = 0
targetNumberMax = 0
scene = "title"
imgMix = 0


# マウスクリック
def mouseClick(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y
    targetDestroy()


# テキスト表示
def text(x, y, text, size, color, tag):
    fontNumber = ("MV Boli", size)
    cvs.create_text(x, y, text=text, font=fontNumber, fill=color, tag=tag)


# スコア、タイマーセット（ループ）
def main():
    global score, timer, scene
    cvs.delete("score")
    cvs.delete("timer")
    text(200, 100, "SCORE:" + str(score), 30, "White", tag="score")
    text(1080, 100, "LIMIT:" + str(timer), 30, "White", tag="timer")
    if timer == 0:
        print("GAME OVER")
        scene = "gameover"
    timer = timer - 1
    root.after(330, main)


# ターゲット破壊
def targetDestroy():
    global mouseX, mouseY, targetNumber, targetList, score
    count = 0
    for n in targetList:
        # ターゲット位置とマウス位置の判定
        if (n.posX - n.size) <= mouseX <= (n.posX + n.size) and (
            n.posY - n.size
        ) <= mouseY <= (n.posY + n.size):
            # スコアカウント
            score += n.score
            targetShakeList.append(targetList.pop(count))
            shakeTarget()
            # ターゲットリストのカウントアップ
            if len(targetList) <= 0:
                if (targetNumber + 1) < targetNumberMax:
                    targetNumber += 1
                else:
                    targetNumber = 0
                    print(f"else:{targetNumber}")
                createObj()
            break
        else:
            count += 1

def shakeTarget():
        global targetShakeList
        # ターゲットアニメーション
        for n in targetShakeList:
            shake(n.tag)
            n.after(10,lambda:cvs.delete(n.tag))
            # ターゲット破壊
            
            # リストからターゲット削除



# ターゲット作成
def createObj():
    global posX, posY, targetList, targetInfoList, targetNumberMax, targetNumber,imgMix
    countTag = 0  # タグ付け用カウント
    targetNumberMax = len(targetInfoList)
    cvs.delete("all")
    cvs.create_image(W / 2, H / 2, image=bgimg)
    cvs.pack()
    currentTarget = targetInfoList[targetNumber]  # ターゲットインスタンスの抽出
    currentNum = int(currentTarget.num)  # ターゲットの生成数取得
    if currentNum == 1:  # Target1の生成
        target = Target(
            W / 2,
            H / 2,
            currentTarget.size,
            currentTarget.score,
            currentTarget.img,
            tag=f"{currentTarget.name}{countTag}",
        )
        cvs.create_image(W / 2, H / 2, image=currentTarget.img, tag=f"{currentTarget.name}{countTag}")
        targetList.append(target)
    elif currentNum == 2:  # Target2の生成
        for n in range(currentNum):
            posX = int(random.randint(currentTarget.size, W / 2)) + ((W / 2) * n)
            if posX + currentTarget.size > W:
                posX = W - currentTarget.size
            posY = int(random.randint(currentTarget.size, H))
            if posY + currentTarget.size > H:
                posY = H - currentTarget.size
            target = Target(
                posX,
                posY,
                currentTarget.size,
                currentTarget.score,
                currentTarget.img,
                tag=f"{currentTarget.name}{countTag}",
            )
            cvs.create_image(posX, posY, image=currentTarget.img, tag=f"{currentTarget.name}{countTag}")
            targetList.append(target)
            countTag += 1
    elif 2 < currentNum <= targetInfoList[-1].num:  # Target3以降の生成
        i = targetNumber - 1
        j = 2**i
        k = int(currentNum / j)
        for n in range(0, k, 1):
            for m in range(0, k, 1):
                posX = int(random.randint(currentTarget.size, W / k)) + ((W / k) * n)
                if posX + currentTarget.size > W:
                    posX = W - currentTarget.size
                posY = int(random.randint(currentTarget.size, H / k)) + ((H / k) * m)
                if posY + currentTarget.size > H:
                    posY = H - currentTarget.size
                
                #img5ランダム設定
                if currentTarget.name == "target5":
                        imgMix = random.randrange(len(imgList))
                        currentTarget.img = imgList[imgMix]
                
                #ターゲット生成
                target = Target(
                    posX,
                    posY,
                    currentTarget.size,
                    currentTarget.score,
                    currentTarget.img,
                    tag=f"{currentTarget.name}{countTag}",
                )
                
                cvs.create_image(
                    posX, posY, image=currentTarget.img, tag=f"{currentTarget.name}{countTag}"
                )
                targetList.append(target)
                countTag += 1


# ターゲット右揺れ
def moveRight(tag):
    cvs.move(tag, 0.2, 0)
    cvs.after(50, lambda: moveLeft(tag))


# ターゲット左揺れ
def moveLeft(tag):
    cvs.move(tag, -0.2, 0)
    cvs.after(50, lambda: moveRight(tag))


# ターゲット左右揺れ
def shake(tag):
    for _ in range(5):
        moveRight(tag)


# ターゲットインスタンス
class Target:
    def __init__(self, posX=0, posY=0, size=0, score=0, img="img", tag="tag"):
        self.posX = posX
        self.posY = posY
        self.size = size
        self.score = score
        self.img = img
        self.tag = tag


# ターゲット情報
class TargetInfo:
    def __init__(self, name="name", num=0, score=0, size=0, img="img"):
        self.name = name
        self.num = num
        self.score = score
        self.size = size
        self.img = img


root = tk.Tk()
root.geometry(f"{W}x{H}")
root.bind("<Button>", mouseClick)
cvs = tk.Canvas(root, width=W, height=H, bg="white")
bgimg = tk.PhotoImage(file="Test2/image/bg.png")

img1 = tk.PhotoImage(file="Test2/image/obj1.png")
img2 = tk.PhotoImage(file="Test2/image/obj2.png")
img3 = tk.PhotoImage(file="Test2/image/obj3.png")
img4 = tk.PhotoImage(file="Test2/image/obj4.png")
img5 = tk.PhotoImage(file="Test2/image/obj5.png")
img5_2=tk.PhotoImage(file="Test2/image/obj6.png")
imgList=[img5,img5_2]


target1 = TargetInfo("target1", 1, 1, 400, img1)
target2 = TargetInfo("target2", 2, 2, 300, img2)
target3 = TargetInfo("target3", 4, 4, 100, img3)
target4 = TargetInfo("target4", 16, 8, 30, img4)
target5 = TargetInfo("target5", 64, 16, 10, img5)
targetInfoList = [target1, target2, target3, target4, target5]


main()
createObj()
root.mainloop()
