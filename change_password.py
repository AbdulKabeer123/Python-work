from tkinter import *


class parent_dash:
    pass
    def exit(self):
        pass
    def clear(self):
        pass

class changeclass(parent_dash):
    def __init__(self, pass_change_page):
        self.pass_change_page = pass_change_page
        self.pass_change_page.title("Lobby")
        self.pass_change_page.config(bg="white")
        self.pass_change_page.geometry('900x550+120+20')
        self.pass_change_page.resizable('false', 'false')

        self.frame_main_heading = Frame(self.pass_change_page, bg="#2ECC71", height='70', width=900)
        self.frame_main_heading.place(x=0, y=0)

        self.lbl_heading = Label(self.frame_main_heading, text="Grocery Management System", fg="white", bg="#2ECC71", font=('times new roman', 20))
        self.lbl_heading.place(x=300, y=20)


        self.second_frame_btn = Frame(self.pass_change_page, width=900, height=50, bg="#27AE60")
        self.second_frame_btn.place(x=0, y=70)

# ======================= Main Frame =======================
        self.fram = Frame(pass_change_page, bg="white")
        self.fram.place(x=230, y=150, width=600, height=500)

        # ======================= labels  =======================
        self.lbl_heading = Label(self.fram, text="change password", font=('times new roman', 20, 'bold'), bg="black",
                                 fg="white")
        self.lbl_heading.pack(fill=X, side=TOP)

        self.lbl_first_name = Label(self.fram, bg="white", text="User Name ", font=('times new roman', 20, 'bold'))
        self.lbl_first_name.place(x=50, y=70)
        self.lbl_contact = Label(self.fram, text="Old password", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_contact.place(x=400, y=70)
        self.lbl_last_name = Label(self.fram, text="New Password", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_last_name.place(x=50, y=140)
        self.lbl_email = Label(self.fram, text="Conf Password", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_email.place(x=400, y=140)

        self.txt_user_name = Entry(self.fram, font=('times new roman', 15, 'bold'),
                                   borderwidth=3)
        self.txt_user_name.place(x=20, y=110)

        self.txt_old_pass = Entry(self.fram, font=('times new roman', 15, 'bold'),
                                   borderwidth=3)
        self.txt_old_pass.place(x=20, y=190)

        self.txt_new_pass = Entry(self.fram, font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_new_pass.place(x=380, y=110)

        self.txt_conf_password2 = Entry(self.fram, font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_conf_password2.place(x=380, y=190)

        self.btn_login = Button(self.fram, text="Change Pass", font=('times ', 15, 'bold'), bg="white",
                                width=13)
        self.btn_login.place(x=220, y=250)

if __name__ == '__main__':
    pass_change_page = Tk()
    obj = changeclass(pass_change_page)
    pass_change_page.mainloop()