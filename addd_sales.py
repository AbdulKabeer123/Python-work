from tkinter import *
from tkinter import messagebox
from time import strftime
from tkinter import ttk
from datetime import datetime
# from openpyxl import workbook
# from openpyxl import load_workbook

class add_class:
    def __init__(self, add_sale):
        self.add_sale = add_sale
        self.add_sale.title("Customer Table")
        self.add_sale.geometry('1030x550+20+20')
        self.add_sale.resizable('false', 'false')
        self.add_sale.config(bg='light blue')
# ============================= Headings ======================================
        self.lbl_heading = Label(self.add_sale, text="Buy Product", font=('arial', 25, 'bold'), bd=10, relief=GROOVE, pady=10)
        self.lbl_heading.pack(fill=X, side=TOP)
# ================================= frame =========================================
        self.fram = Frame(self.add_sale, width=500, height=400, relief=GROOVE, bd=10)
        self.fram.place(x=5, y=80)

# ================================= frame's customer dat==a lbls =======================================
        self.lbl_first_name = Label(self.fram, text="Customer Data", font=('times new roman', 20, 'bold'), fg="white",  bg="Black")
        self.lbl_first_name.place(x=135, y=10)

        self.lbl_first_name = Label(self.fram, text="Name", font=('times new roman', 20, 'bold'))
        self.lbl_first_name.place(x=10, y=60)

        self.lbl_contact = Label(self.fram, text="Email", font=('times new roman', 20, 'bold'))
        self.lbl_contact.place(x=10, y=120)

        self.lbl_last_name = Label(self.fram, text="Contact", font=('times new roman', 20, 'bold'))
        self.lbl_last_name.place(x=10, y=180)

        self.lbl_current_time = Label(self.fram, text="Time", font=('times new roman', 20, 'bold'))
        self.lbl_current_time.place(x=10, y=240)

# ================================ set time ===================================
        def time():
            string = strftime('%H:%M:%S %p')
            day = strftime('%A')
            self.lbl_set_time.config(text=string)
            self.lbl_set_time.after(1000, time)
            self.set_day.config(text=day)

        self.lbl_set_time = Label(self.add_sale, font=('calibri', 20, 'bold'))
        self.lbl_set_time.place(x=223, y=330)

        self.set_day = Label(self.add_sale, font=('calibri', 10, 'bold'))
        self.set_day.place(x=383, y=330)

        time()

# =============================== variables ==================================
        name = StringVar()
        email = StringVar()
        contact = StringVar()
        payment = StringVar()
        duration = StringVar()

# =============================== frame's entries boxes ======================================
        self.txt_first_name = Entry(self.fram, textvariable=name, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_first_name.place(x=210, y=60)

        self.txt_last_name = Entry(self.fram, textvariable=email, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_last_name.place(x=210, y=120)

        self.txt_contact = Entry(self.fram, textvariable=contact, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_contact.place(x=210, y=180)

        # ================================= frame 2 =========================================
        self.fram2 = Frame(self.add_sale, width=500, height=400, relief=GROOVE, bd=10)
        self.fram2.place(x=523, y=80)
        # ================================= frame's lables =======================================

        self.lbl_heading_room_info = Label(self.fram2, text="Add Product", font=('times new roman', 20, 'bold'), fg="white", bg="Black")
        self.lbl_heading_room_info.place(x=135, y=10)

        self.lbl_ = Label(self.fram2, text="Product Name", font=('times new roman', 20, 'bold'))
        self.lbl_.place(x=10, y=60)

        self.lbl_product_type = Label(self.fram2, text="Product Type", font=('times new roman', 20, 'bold'))
        self.lbl_product_type.place(x=10, y=120)

        self.lbl_company = Label(self.fram2, text="Company", font=('times new roman', 20, 'bold'))
        self.lbl_company.place(x=10, y=180)

        self.lbl_qty_product = Label(self.fram2, text="Quantity product", font=('times new roman', 20, 'bold'))
        self.lbl_qty_product.place(x=10, y=240)

        self.lbl_total_bill = Label(self.fram2, text="Total Amount", font=('times new roman', 20, 'bold'))
        self.lbl_total_bill.place(x=10, y=300)

# ========================================= Creating Combo boxes ========================================
        product_name = StringVar()
        self.txt_first_name = Entry(self.fram2, textvariable=product_name, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_first_name.place(x=230, y=60)

        product_type = StringVar()
        self.txt_last_name = Entry(self.fram2, textvariable=product_type, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_last_name.place(x=230, y=120)

        comapny = StringVar()
        self.txt_contact = Entry(self.fram2, textvariable=comapny, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_contact.place(x=230, y=180)

        qty_product = StringVar()
        self.txt_contact = Entry(self.fram2, textvariable=qty_product, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_contact.place(x=230, y=240)

        self.product_price = IntVar()
        self.txt_price = Entry(self.fram2, textvariable=self.product_price, bg="silver", font=('times new roman', 15, 'bold'), borderwidth=3)
        self.txt_price.place(x=230, y=300)

# =============================== time show =====================================
        current = datetime.now()
        current_time = current.now()
        current_time = current.strftime("%H" + ":" + "%M" + ":" + "%S")

        '''def submit():
                if name.get() != "" and email.get() != "" and contact.get() != "" and email.get() != "" or payment.get() != "" or duration.get() != "":
                    wb = workbook
                    wb = load_workbook('record2.xlsx')
                    work_sheet = wb.active
                    work_sheet["A1"] = "Name \n "
                    work_sheet["B1"] = "Email \n "
                    work_sheet["C1"] = "Contact \n "
                    work_sheet["D1"] = "Payment \n "
                    work_sheet["E1"] = "Duration \n "
                    work_sheet["F1"] = "Room QTY \n "
                    work_sheet["G1"] = "Room Size \n "
                    work_sheet["H1"] = "Parking \n "
                    work_sheet["I1"] = "AC \n "
                    work_sheet["J1"] = "Room NO \n "

                    work_sheet.cell(column=1, row=work_sheet.max_row + 1, value=name.get())
                    work_sheet.cell(column=2, row=work_sheet.max_row, value=email.get())
                    work_sheet.cell(column=3, row=work_sheet.max_row, value=contact.get())
                    work_sheet.cell(column=4, row=work_sheet.max_row, value=payment.get())
                    work_sheet.cell(column=5, row=work_sheet.max_row, value=duration.get())
                    work_sheet.cell(column=6, row=work_sheet.max_row, value=self.room_qty.get())
                    work_sheet.cell(column=7, row=work_sheet.max_row, value=self.room_size.get())
                    work_sheet.cell(column=8, row=work_sheet.max_row, value=self.parking.get())
                    work_sheet.cell(column=9, row=work_sheet.max_row, value=self.air_condition.get())
                    work_sheet.cell(column=10, row=work_sheet.max_row, value=self.room_no.get())


                    #                wb.save('record.xlsx')

                    print(name.get())
                    print(email.get())
                    print(contact.get())
                    print(payment.get())
                    print(duration.get())
                    print(self.room_qty.get())
                    print(self.room_size.get())
                    print(self.parking.get())
                    print(self.air_condition.get())
                    print(self.room_no.get())
                    #                wb.save('record.xlsx')
                    wb.save('record2.xlsx')
                    messagebox.showinfo('info', "you data save in excel data sheet")
                else:
                    messagebox.showerror('error', 'Something Went wrong')'''
        def reset():
            msg = messagebox.askquestion('Exit Application', 'are you sure to exit this page')
            if msg == 'yes':
                name.set("")
                email.set("")
                contact.set("")
                payment.set("")
                duration.set("")

        def exit():
            msg = messagebox.askquestion('Exit Application', 'are you sure to exit this page')
            if msg == 'yes':
                add_sale.destroy()

        self.btn_submit = Button(self.add_sale, text="Submit", font=('times new roman', 20, 'bold'), width=17, height=1)
        self.btn_submit.place(x=10, y=487)

        self.btn_reset = Button(self.add_sale, text="Clear", command=reset, font=('times new roman', 20, 'bold'), width=17, height=1)
        self.btn_reset.place(x=335, y=487)

        self.btn_reset = Button(self.add_sale, text="Exit", command=exit, font=('times new roman', 20, 'bold'), width=17, height=1)
        self.btn_reset.place(x=655, y=487)




if __name__ == '__main__':
    add_sale = Tk()
    obj = add_class(add_sale)
    add_sale.mainloop()