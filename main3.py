import tkinter as tk
import random
import requests
import json

W, H = 1280, 720
listNum = 0


def text(x, y, text, size, color):
    fontC = ("", size)
    root.create_text(x, y, text=text, font=fontC, fill=color)



def main():
    displayProverb()
    frame2.place(anchor="center", x=W / 2, y=H / 2)  # frame配置
    mainLabel.place(anchor="sw", x=210, y=700, relwidth=0.8, relheight=0.3)
    faceCVS.place(
        anchor="sw",
        x=50,
        y=705,
    )


def destroy():
    frame2.place_forget()
    faceCVS.delete()
    replaceSecond = random.randint(1, 10) * 1000
    root.after(replaceSecond, replace)


def replace():
    mainLabel["text"] = displayProverb()
    faceCVS.create_image(80, 110, image=faceImgList[listNum])
    frame2.place(anchor="center", x=W / 2, y=H / 2)
    root.after(2000, destroy)


class Proverb:
    def __init__(self, name, word):
        self.name = name
        self.word = word


def appendProverbs(url, name):
        res = requests.get(url)
        data = json.loads(res.text)
        proverb=Proverb(name, data["text"])
        return proverb


def appendProverbsFirst(url, name):
        res = requests.get(url)
        data = json.loads(res.text)
        worddata = data["slip"]["advice"]
        proverb=Proverb(name, worddata)
        return proverb


def appendProverbsSecond(url, name):
        res = requests.get(url)
        data = json.loads(res.text)
        setup = data["setup"]
        punchline = data["punchline"]
        texts = f"{setup} \n{punchline}"
        proverb=Proverb(name, texts)
        return proverb


def appendProverbsThird(url, name):
        res = requests.get(url)
        data = json.loads(res.text)
        proverb=Proverb(name, data["activity"])
        return proverb


# テキスト表記のための乱数、テキスト作成
def displayProverb():
    global listNum
    listNum = random.randrange(len(faceImgList))
    if listNum == 0:
        proverb=appendProverbsSecond(url1, "Oldman")  # APIから情報を取得
    elif listNum == 1:
        proverb=appendProverbs(url2, "Scientist")
    elif listNum == 2:
        proverb=appendProverbsFirst(url3, "OldWoman")
    elif listNum == 3:
        proverb=appendProverbsThird(url4, "Boy")  
    mainText = f"{proverb.name}\n{proverb.word}"
    return mainText


root = tk.Tk()
fontA = ("Family", 50)
root.geometry("1280x720")
root.title("x")
frame2 = tk.Frame(root, width=W, height=H)
frame2.propagate(False)

frameImg = tk.PhotoImage(file="Test2/image/frame.png")
faceImg1 = tk.PhotoImage(file="Test2/image/oldman.png")
faceImg2 = tk.PhotoImage(file="Test2/image/scientist.png")
faceImg3 = tk.PhotoImage(file="Test2/image/oldwoman.png")
faceImg4 = tk.PhotoImage(file="Test2/image/boy.png")

faceImgList = [faceImg1, faceImg2, faceImg3, faceImg4]


url1 = "https://official-joke-api.appspot.com/jokes/random"
url2 = "http://numbersapi.com/random/year?json"
url3 = "https://api.adviceslip.com/advice"
url4 = "https://www.boredapi.com/api/activity/"

mainLabel = tk.Label(
    frame2,
    width=1025,
    height=220,
    compound=tk.CENTER,
    text=displayProverb(),
    image=frameImg,
    fg="red",
    font=("Family", 20),
)
faceCVS = tk.Canvas(frame2, width=160, height=220)
# faceCVS.create_image(80, 110, image=faceImgList[listNum])


root.after(3000, main)
root.after(6000, destroy)
root.mainloop()
