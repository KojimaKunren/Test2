import tkinter as tk

W,H = 1280,720
scene = "title"
score,timer=0,0
mouseClick=False

def click(e):
    global mouseClick
    mouseClick=True

def text(x,y,text,size,color):
    fontA=("Family",size)
    titleCVS.create_text(x,y,text=text,font=fontA,fill=color)

def init():
    global score, timer, scene, mouseClick
    titleCVS.delete("all")
    titleCVS.create_image(640,360,image=titleImg)
    if scene=="title":
        text(W/2,H*0.6,"Click to Start",50,"red")
        if(mouseClick==True):
            scene="game"
            score=0
            timer=60
            mouseClick=False
            

    if scene=="game":
        main()

    if scene=="gameover":
        titleCVS.create_image(W/2,H/2,image=bgImg)
        text(W/2,H*0.4,f"SCORE:{score}",60,"White")
        text(W/2,H*0.6,"Click to ReStart",30,"red")
        if(mouseClick==True):
            scene="game"
            score=0
            timer=60
            mouseClick=False
   
    root.after(50,init)

def main():
    print(f"mainが実行されました")

root=tk.Tk()
root.geometry(f"{W}x{H}")
root.bind("<Button>",click)

titleCVS = tk.Canvas(width=W,height=H)
titleImg=tk.PhotoImage(file="Test2/image/start.png")
bgImg=tk.PhotoImage(file="Test2/image/bg.png")
titleCVS.pack()

init()
root.mainloop()