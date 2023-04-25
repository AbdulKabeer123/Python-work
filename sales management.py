from tkinter import*
class sales:
    def sales_managemebt(self):
        root = Tk()
        root.configure(bg="white")
        root.title("Add sales")
        cuslab = Label(root,text="customer details",font=16).place(x=40,y=50)
        cusname = Label(root,text="customer Name",font=16).place(x=40,y=100)
        nameent = Entry(root).place(x=200,y=100)
        cuscon = Label(text="customer contact",font=16).place(x=40,y=150)
        content = Entry(root).place(x=200,y=150)

        add_but = Button(root,text = "Add Customer",bg="green").place(x=40,y=200)


        root.mainloop()