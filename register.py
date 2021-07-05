from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("300x300")
root.config(bg = "dark slate grey")

class Register:
    def __init__(self,master):
        self.user_reg_label = Label(master, text = 'Enter name:')
        self.user_reg_label.place(x= 20, y= 50)
        self.user_reg_entry = Entry(master)
        self.user_reg_entry.place(x = 100, y = 50)

        self.pass_reg_label = Label(master, text = 'Enter surname:')
        self.pass_reg_label.place(x = 20 , y = 150)
        self.pass_reg_entry = Entry(master)
        self.pass_reg_entry.place(x = 100 , y = 150)

        self.password_label = Label(master, text = 'Create password: ')
        self.password_label.place(x=20 , y = 200)
        self.password_entry = Entry(master)
        self.password_entry.place(x=100 , y= 200)

        self.cell_number_label = Label(master, text = 'Enter cell number')
        self.cell_number_label.place(x= 20 , y = 250)
        self.cell_number_entry = Entry(master)
        self.cell_number_entry.place(x=100, y=250)




        self.reg_btn = Button(master, text = "Register", command = self.reg)
        self.reg_btn.place(x= 50, y=250)

    def reg(self):
        if self.pass_reg_entry.get() == "" or self.user_reg_entry.get() == "":
            messagebox.showwarning(title='Invalid', message='Please enter valid details.')
        elif self.pass_reg_entry.get() == " " or self.user_reg_entry.get() == " ":
            messagebox.showwarning(title="Space", message="Please enter valid details.")


        else:

            mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="siSVLIJkL8", password="sql4423111", database="sql4423111", auth_plugin = 'mysql_native_password')

            mycursor = mydb.cursor()

            sql = "INSERT INTO register (name, surname, password, phone_number) VALUES (%s, %s, %s, %s)"
            val = (self.user_reg_entry.get(), self.pass_reg_entry.get(),self.password_entry.get(),self.cell_number_entry.get())
            mycursor.execute(sql, val)

            mydb.commit()
            messagebox.showinfo(title="Valid", message='Enter next of keen details.')
            import next_if_keen_table
            root.destroy()

x = Register(root)
root.mainloop()


