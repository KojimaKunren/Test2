import tkinter as tk

W, H = 1280, 720


def main():
    cvs1.place(anchor="center", x=640, y=580, relwidth=0.8, relheight=0.3)
    cvs2.create_text(
        35, 15, text="aaa", anchor="center", font=("Family", 17), fill="red"
    )
    cvs2.place(anchor="center", x=270, y=490)
    cvs3.create_image(50, 50, image=img)
    cvs3.place(anchor="center", x=181, y=576)


def update():
    cvs1.itemconfig("cvs1", text="ccc")
    root.after(2000, destroy)


def destroy():
    cvs1.place_forget()
    cvs2.place_forget()
    cvs3.place_forget()
    root.after(2000, replace)


def replace():
    cvs1.place(anchor="center", x=640, y=580, relwidth=0.8, relheight=0.3)
    cvs2.place(anchor="center", x=270, y=490)
    cvs3.place(anchor="center", x=181, y=576)


root = tk.Tk()
fontA = ("Family", 50)
root.geometry("1280x720")
root.title("x")

cvs1 = tk.Canvas(root, width=1000, height=50, bg="black")
cvs1.create_text(
    180, 80, text="bbb", anchor="e", font=("Family", 30), fill="red", tag="cvs1"
)

cvs2 = tk.Canvas(root, width=70, height=30, bg="gray")

cvs3 = tk.Canvas(root, width=100, height=200, bg="skyblue")

img = tk.PhotoImage(file="Test2/obj5.png")

main()
root.after(5000, update)
root.mainloop()
