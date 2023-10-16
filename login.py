#! C:/Users/0609PM/AppData/Local/Programs/Python/Python311/python.exe
# -*- coding: utf-8 -*-
print("Content-Type:text/html\n")

import tkinter as tk
import dao

W, H = 1280, 720
username = ""
password = ""
currentuser = None
newuser = None
isClick = False


class User:
    def __init__(self, id, username, password, topscore, secondscore, thirdscore):
        self.id = id
        self.username = username
        self.password = password
        self.topscore = topscore
        self.secondscore = secondscore
        self.thirdscore = thirdscore


class NewUser:
    def __init__(self, username, password, topscore, secondscore, thirdscore):
        self.username = username
        self.password = password
        self.topscore = topscore
        self.secondscore = secondscore
        self.thirdscore = thirdscore


def getUser():
    global currentuser, newuser
    userdata = dao.find_all()
    for n in userdata:
        # ユーザーの検索、パスワードの確認、現在のユーザーに設定
        if n["username"] == username and n["password"] == password:
            currentuser = User(
                n["id"],
                n["username"],
                n["password"],
                n["topscore"],
                n["secondscore"],
                n["thirdscore"],
            )
            data = dao.find_one(currentuser)
            currentuser.topscore = data.topscore
            currentuser.secondscore = data.secondscore
            currentuser.thirdscore = data.thirdscore

            break
        # 新規ユーザー登録
        else:
            newuser = NewUser(username, password, 0, 0, 0)
            dao.insert_one(newuser)
            setUser()


# 新規ユーザーを現在のユーザーに設定
def setUser():
    global currentuser, newuser
    userdata = dao.find_one(newuser)
    currentuser = User(
        userdata[0],
        userdata[1],
        userdata[2],
        userdata[3],
        userdata[4],
        userdata[5],
    )


def getEntry():
    global username, password
    username = nameEntry.get()
    password = passEntry.get()


root = tk.Tk()
root.geometry(f"{W}x{H}")
frame = tk.Frame(root, width=W, height=H / 2)
font = ("Family", 20)
nameEntry = tk.Entry(frame)
passEntry = tk.Entry(frame)
nameLabel = tk.Label(frame, text="USER NAME", font=font, fg="Black")
passLabel = tk.Label(frame, text="Password", font=font, fg="Black")
button = tk.Button(frame, text="SEND", command=getEntry())
nameLabel.pack()
nameEntry.pack()
passLabel.pack()
passEntry.pack()
button.pack()
frame.place(anchor="center", x=W / 2, y=H * 0.2)

getEntry()
getUser()
print(currentuser.topscore)
root.mainloop()
