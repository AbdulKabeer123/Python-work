from tkinter import *
from tkinter import ttk
# import mysql.connector

class purchase:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.config(bg="white")
        self.root.geometry('810x450+120+20')
        self.root.resizable('false', 'false')

        self.frame_main_heading = Frame(self.root, bg="#2ECC71", height='70', width=840)
        self.frame_main_heading.place(x=0, y=0)

        self.lbl_heading = Label(self.frame_main_heading, text="Grocery Management System", fg="white", bg="#2ECC71", font=('times new roman', 20))
        self.lbl_heading.place(x=220, y=20)

        '''def show_data():
            conn = mysql.connector.connect(host="localhost", user="root", database="sms")
            cursor = conn.cursor()
            cursor.execute("select * from student_data")
            data = cursor.fetchall()
            if len(data) != 0:
                self.std_table.delete(*self.std_table.get_children())
                for i in data:
                    self.std_table.insert("", END, values=i)
                    conn.commit()
                conn.close()'''

        treeview_frame = Frame(self.root)
        treeview_frame.place(x=20, y=90, width=810, height=200)

        treeview_frame = LabelFrame(self.root, text="Purchased Record", font=("arial", 11, "bold"), relief=RIDGE, bd=4,
                                    bg="white")
        treeview_frame.place(x=0, y=90, width=810, height=200)

        scroll_x = ttk.Scrollbar(treeview_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(treeview_frame, orient=VERTICAL)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", forebackground="yellow",
                        fieldbackground="white")
        style.map("Treeview", background=[('selected', '#074463')])
        self.std_table = ttk.Treeview(treeview_frame, columns=("Name", "Email", "Contact", "Contact", "Product_Name", "Product_type", "Company", "Qty_Product", "Total_Amount"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.std_table.xview)
        scroll_y.config(command=self.std_table.yview)


        self.std_table.heading("Name", text="Name")
        self.std_table.heading("Email", text="Email")
        self.std_table.heading("Contact", text="Contact")
        self.std_table.heading("Product_Name", text="Product Name")
        self.std_table.heading("Product_type", text="Product type")
        self.std_table.heading("Company", text="Company")
        self.std_table.heading("Qty_Product", text="Qty_Product")
        self.std_table.heading("Total_Amount", text="Total_Amount")
        self.std_table["show"] = "headings"

        self.std_table.column("Name", width=50)
        self.std_table.column("Email", width=120)
        self.std_table.column("Contact", width=120)
        self.std_table.column("Product_Name", width=60)
        self.std_table.column("Product_type", width=80)
        self.std_table.column("Company", width=100)
        self.std_table.column("Qty_Product", width=80)
        self.std_table.column("Total_Amount", width=80)
        self.std_table.pack(fill=BOTH, expand=1)
        # show_data()

if __name__ == '__main__':
    root = Tk()
    obj = purchase(root)
    root.mainloop()