import tkinter as tk
import random
import requests
import json

W, H = 1280, 720
listNum = 0

def text(x,y,text,size,color):
    fontC=("",size)
    root.create_text(x,y,text=text,font=fontC,fill=color)

def initProverbs():
    appendProverbsSecond(0,url1,"Oldman") #APIから情報を取得
    appendProverbs(1,url2,"Scientist")
    appendProverbsFirst(2,url3,"OldWoman")
    appendProverbsThird(3,url4,"Boy")


def main():
    displayProverb(proverbsList)
    frame2.place(anchor="center", x=W/2, y=H/2) #frame配置
    mainLabel.place(anchor="sw", x=210, y=700, relwidth=0.8, relheight=0.3)
    faceCVS.place(anchor="sw", x=50, y=705,)

    
def destroy():
    frame2.place_forget()
    faceCVS.delete()
    replaceSecond=random.randint(1,10)*1000
    root.after(replaceSecond, replace)


def replace():
    mainLabel["text"]=displayProverb(proverbsList)
    faceCVS.create_image(80,110, image=actualFaceImg)
    frame2.place(anchor="center", x=W/2, y=H/2)
    root.after(2000,destroy)
    

class Proverb:
    def __init__(self,name,word):
        self.name=name
        self.word=word

def appendProverbs(num,url,name):
    for n in range(10):
        res=requests.get(url)
        data=json.loads(res.text)
        proverbsList[num].append(Proverb(name,data['text']))
        print(proverbsList[num][n].word)

def appendProverbsFirst(num,url,name):
    for n in range(10):
        res=requests.get(url)
        data=json.loads(res.text)
        worddata=data['slip']['advice']
        proverbsList[num].append(Proverb(name,worddata))
        print(proverbsList[num][n].word)

def appendProverbsSecond(num,url,name):
    for n in range(10):
        res=requests.get(url)
        data=json.loads(res.text)
        setup=data['setup']
        punchline=data['punchline']
        texts=setup +"/n"+ punchline
        proverbsList[num].append(Proverb(name,texts))
        print(proverbsList[num][n].word)

def appendProverbsThird(num,url,name):
    for n in range(10):
        res=requests.get(url)
        data=json.loads(res.text)
        proverbsList[num].append(Proverb(name,data['activity']))
        print(proverbsList[num][n].word)

#テキスト表記のための乱数、テキスト作成
def displayProverb(proverbsList):
    global listNum
    listNum = random.randint(0,3)
    print(proverbsList[listNum][0].word)
    # listpick = proverbsList[listNum] 
    wordNum = random.randint(0,9)
    # listpickNum= listpick[wordNum]
    displayname = proverbsList[listNum][wordNum].name
    displayword = proverbsList[listNum][wordNum].word
    mainText=f"{displayname}/n{displayword}"
    return mainText

root = tk.Tk()
fontA = ("Family", 50)
root.geometry("1280x720")
root.title("x")
frame2 = tk.Frame(root,width=W,height=H)
frame2.propagate(False)

frameImg = tk.PhotoImage(file="Test2/image/frame.png")
faceImg1 = tk.PhotoImage(file="Test2/image/oldman.png")
faceImg2 = tk.PhotoImage(file="Test2/image/scientist.png")
faceImg3 = tk.PhotoImage(file="Test2/image/oldwoman.png")
faceImg4 = tk.PhotoImage(file="Test2/image/boy.png")

faceImgList=[
    faceImg1,faceImg2,faceImg3,faceImg4
]


proverbs1=[]
proverbs2=[]
proverbs3=[]
proverbs4=[]

proverbsList =[
    proverbs1,proverbs2,proverbs3,proverbs4
]

mainLabel = tk.Label(frame2, width=1025, height=220, compound=tk.CENTER, text=displayProverb(proverbsList), image=frameImg, fg="red", font=("Family",20))
faceCVS = tk.Canvas(frame2, width=160, height=220)
actualFaceImg = faceImgList[listNum]
faceCVS.create_image(80,110, image=actualFaceImg)

url1="https://official-joke-api.appspot.com/jokes/random"
url2="http://numbersapi.com/random/year?json"
url3="https://api.adviceslip.com/advice"
url4="https://www.boredapi.com/api/activity/"

initProverbs()
root.after(3000,main)
root.after(6000, destroy)
root.mainloop()