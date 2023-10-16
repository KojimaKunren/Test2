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
    for n in userdata():
        # ユーザーの検索、パスワードの確認、現在のユーザーに設定
        if userdata[n].username == username and userdata[n].password == password:
            currentuser = User(
                userdata[n]["id"],
                userdata[n]["username"],
                userdata[n]["password"],
                userdata[n]["topscore"],
                userdata[n]["secondscore"],
                userdata[n]["thirdscore"],
            )
        # 新規ユーザー登録
        else:
            newuser = NewUser(0, username, password, 0, 0, 0)
            dao.insert_one(newuser)
            setUser()


# 新規ユーザーを現在のユーザーに設定
def setUser():
    global currentuser, newuser
    userdata = dao.find_one(newuser.name)
    for n in userdata():
        currentuser = User(
            userdata[n]["id"],
            userdata[n]["username"],
            userdata[n]["password"],
            userdata[n]["topscore"],
            userdata[n]["secondscore"],
            userdata[n]["thirdscore"],
        )


root = tk.Tk()
root.geometry(f"{W}x{H}")
frame = tk.Frame(root, width=W, height=H / 2)
font = ("Family", 20)
nameEntry = tk.Entry(frame)
passEntry = tk.Entry(frame)
nameLabel = tk.Label(frame, text="USER NAME", font=font, fg="Black")
passLabel = tk.Label(frame, text="Password", font=font, fg="Black")
nameLabel.pack()
nameEntry.pack()
passLabel.pack()
passEntry.pack()
username = nameEntry.get()
password = passEntry.get()
frame.place(anchor="center", x=W / 2, y=H * 0.2)

getUser()
root.mainloop()
