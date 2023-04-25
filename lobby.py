from tkinter import *
from addrecord import add_record
from addd_sales import add_class
from purchaseview import purchase
# from purchaseview import purchase_view
class parent_dash:
    pass
    def exit(self):
        pass
    def clear(self):
        pass

class dash(parent_dash):
    def __init__(self, lobby_page):
        self.lobby_page = lobby_page
        self.lobby_page.title("Lobby")
        self.lobby_page.config(bg="white")
        self.lobby_page.geometry('900x550+120+20')
        self.lobby_page.resizable('false', 'false')

        self.frame_main_heading = Frame(self.lobby_page, bg="#2ECC71", height='70', width=900)
        self.frame_main_heading.place(x=0, y=0)

        self.lbl_heading = Label(self.frame_main_heading, text="Grocery Management System", fg="white", bg="#2ECC71", font=('times new roman', 20))
        self.lbl_heading.place(x=300, y=20)

        self.second_frame_btn = Frame(self.lobby_page, width=900, height=50, bg="#27AE60")
        self.second_frame_btn.place(x=0, y=70)

        # ========= radio buttons
        self.hole_menu = Menu(self.lobby_page)
        self.lobby_page.config(menu=self.hole_menu)

        self.file_menu = Menu(self.hole_menu, tearoff="false")
        self.hole_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Add Record", command=self.open_addrecord)
        self.file_menu.add_command(label="View Record")
        self.file_menu.add_command(label="Exit", command=self.lobby_page.quit)
        self.edit_menu = Menu(self.hole_menu, tearoff="false")

####____________________________button_____________________________#### lobby page____________#####

        self.btn_home = Button(self.second_frame_btn, text="ADD Product ",  command=self.open_addrecord, font=('times ', 10),
                               bg="#27AE60", bd=0, width=22, fg="white")
        self.btn_home.place(x=50, y=3)

        self.btn_home = Button(self.second_frame_btn, text="View Product ", command=self.open_viewrecord, font=('times ', 10),
                               bg="#27AE60", bd=0, width=22, fg="white")
        self.btn_home.place(x=175, y=3)

        self.btn_home = Button(self.second_frame_btn, text="ADD Sales ", command=self.open_record, font=('times ', 10), bg="#27AE60", bd=0,
                               width=22, fg="white")
        self.btn_home.place(x=300, y=3)

        self.btn_home = Button(self.second_frame_btn, text="Sales Record ", font=('times ', 10), bg="#27AE60", bd=0,
                               width=22, fg="white")
        self.btn_home.place(x=425, y=3)

        self.btn_home = Button(self.second_frame_btn, text="LogOut", command=self.exit_fun, font=('times ', 10), bg="#27AE60", bd=0, width=13,
                               fg="white")
        self.btn_home.place(x=570, y=3)

    def exit_fun(self):
        self.lobby_page.destroy()
    def open_addrecord(self):
        lobby_variable = Toplevel(self.second_frame_btn)
        open_lobby = add_record(lobby_variable)
    def open_record(self):
        addrecord_variable = Toplevel(self.second_frame_btn)
        open_lobby = add_class(addrecord_variable)
    def open_viewrecord(self):
        openbut = Toplevel(self.second_frame_btn)
        open_view_record = purchase(openbut)

if __name__ == '__main__':
    lobby_page = Tk()
    obj = dash(lobby_page)
    lobby_page.mainloop()