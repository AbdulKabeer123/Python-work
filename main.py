from tkinter import *
from PIL import  ImageTk
from lobby import dash
from tkinter import messagebox

class parent_login:
    pass

class login(parent_login):
    def __init__(self, login_page):
        self.login_page = page
        self.login_page.title("Login Page")
        self.login_page.config(bg="white")
        self.login_page.geometry('730x450+120+20')
        self.login_page.resizable('false', 'false')

        self.frame_main_heading = Frame(self.login_page, bg="#2ECC71", height='70', width=800)
        self.frame_main_heading.place(x=0, y=0)

        self.lbl_heading = Label(self.frame_main_heading, text="Grocery Management System", fg="white", bg="#2ECC71", font=('times new roman', 20))
        self.lbl_heading.place(x=190, y=20)

        self.pic_logo = ImageTk.PhotoImage(file="logo_login.png")
        self.pic_lbl = Label(self.login_page, image=self.pic_logo, bd=0, bg="white")
        self.pic_lbl.place(x=300, y=90)

        self.lbl_user = Label(self.login_page, text="User Login", font=('times new roman', 12, 'bold'), bg="white")
        self.lbl_user.place(x=150, y=200)
        self.lbl_password = Label(self.login_page, text="Password", font=('times new roman', 12, 'bold'), bg="white")
        self.lbl_password.place(x=150, y=250)

        txt_admin = StringVar()
        txt_pass = StringVar()
        self.txt_user = Entry(self.login_page, textvariable =txt_admin, font=('times new roman', 12), bd=2, bg='grey')
        self.txt_user.place(x=280, y=200)
        self.txt_user = Entry(self.login_page, textvariable =txt_pass, font=('times new roman', 12), bd=2, bg='grey')
        self.txt_user.place(x=280, y=250)

        def login():
            if txt_admin.get() == "admin" and txt_pass.get() == "admin":
                lobby_variable = Toplevel(self.login_page)
                open_lobby = dash(lobby_variable)

            else:
                messagebox.showerror("error", "wrong putting")
        def clear():
            txt_admin.set("")
            txt_pass.set("")
        self.btn_login = Button(self.login_page, text="Login", command=login, font=('times ', 15, 'bold'), bg="white", width=13)
        self.btn_login.place(x=280, y=320)

        self.btn_login = Button(self.login_page, text="Login", command=clear,  bg="white", width=13, bd=0, fg="red")
        self.btn_login.place(x=380, y=280)

if __name__ == '__main__':
    page = Tk()
    obj = login(page)
    page.mainloop()