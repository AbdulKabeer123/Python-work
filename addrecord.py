from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from abc import ABC,abstractmethod

class parent_dash(ABC):
    def exit(self):
        pass
    def clear(self):
        pass

class add_record(parent_dash):
    def __init__(self, record_page):
        self.record_page = record_page
        self.record_page.title("Lobby")
        self.record_page.config(bg="white")
        self.record_page.geometry('900x550+120+20')
        self.record_page.resizable('false', 'false')

        self.frame_main_heading = Frame(self.record_page, bg="#2ECC71", height='70', width=900)
        self.frame_main_heading.place(x=0, y=0)

        self.lbl_heading = Label(self.frame_main_heading, text="Grocery Management System", fg="white", bg="#2ECC71", font=('times new roman', 20))
        self.lbl_heading.place(x=300, y=20)

        self.second_frame_btn = Frame(self.record_page, width=900, height=50, bg="#27AE60")
        self.second_frame_btn.place(x=0, y=70)
        # ======================= Main Frame =======================
        self.fram = Frame(record_page, bg="white")
        self.fram.place(x=230, y=150, width=600, height=500)

        # ======================= labels  =======================
        self.lbl_heading = Label(self.fram, text="Add Record", font=('times new roman', 20, 'bold'), bg="black", fg="white")
        self.lbl_heading.pack(fill=X, side=TOP)
        self.lbl_first_name = Label(self.fram, bg="white", text="Product ID", font=('times new roman', 20, 'bold'))
        self.lbl_first_name.place(x=50, y=70)
        self.lbl_contact = Label(self.fram, text="Product Name", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_contact.place(x=400, y=70)
        self.lbl_last_name = Label(self.fram, text="Product Price", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_last_name.place(x=50, y=140)
        self.lbl_email = Label(self.fram, text="Product Qty", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_email.place(x=400, y=140)
        self.lbl_password = Label(self.fram, text="Product Company", bg="white", font=('times new roman', 20, 'bold'))
        self.lbl_password.place(x=50, y=230)
        self.lbl_conf_password = Label(self.fram, text="Product Bar Code", bg="white", font=('times new roman', 17, 'bold'))
        self.lbl_conf_password.place(x=400, y=230)

        # ======================= Entries =======================
        self.txt_first_name = Entry(self.fram, font=('times new roman', 15, 'bold'),
                                    borderwidth=3)
        self.txt_first_name.place(x=20, y=110)

        self.txt_last_name = Entry(self.fram, font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_last_name.place(x=20, y=190)

        self.txt_contact = Entry(self.fram, font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_contact.place(x=350, y=110)

        self.txt_email = Entry(self.fram, font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_email.place(x=350, y=190)

        self.txt_passwrod = Entry(self.fram, show='*', font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_passwrod.place(x=20, y=270)

        self.txt_conf_password = Entry(self.fram, font=('times new roman', 15, 'bold'), show='*', borderwidth=3)
        self.txt_conf_password.place(x=350, y=270)

        self.btn_login = Button(self.record_page, text="Add Record", font=('times ', 15, 'bold'), bg="white", width=13)
        self.btn_login.place(x=40, y=400)

        self.btn_login = Button(self.record_page, text="Clear", font=('times ', 15, 'bold'), bg="white", width=13)
        self.btn_login.place(x=40, y=460)

if __name__ == '__main__':
    record_page = Tk()
    obj = add_record(record_page)
    record_page.mainloop()