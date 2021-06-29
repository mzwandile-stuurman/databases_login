from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("300x300")
root.config(bg = "dark slate grey")

class Register:
    def __init__(self,master):
        self.user_reg_label = Label(master, text = 'Enter your username:')
        self.user_reg_label.place(x= 20, y= 50)
        self.user_reg_entry = Entry(master)
        self.user_reg_entry.place(x = 100, y = 50)

        self.pass_reg_label = Label(master, text = 'Enter password to register:')
        self.pass_reg_label.place(x = 20 , y = 150)
        self.pass_reg_entry = Entry(master)
        self.pass_reg_entry.place(x = 100 , y = 150)

        self.reg_btn = Button(master, text = "Register", command = self.reg)
        self.reg_btn.place(x= 50, y=250)

    def reg(self):
        if self.pass_reg_entry.get() == " " or self.user_reg_entry.get() == " ":
            messagebox.showwarning(title='Invalid', message='Please enter valid details.')

        else:

            mydb = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="Hospitals", auth_plugin = 'mysql_native_password')

            mycursor = mydb.cursor()

            sql = "INSERT INTO Login (user, password) VALUES (%s, %s)"
            val = (self.user_reg_entry.get(), self.pass_reg_entry.get())
            mycursor.execute(sql, val)

            mydb.commit()
            messagebox.showinfo(title="Valid", message='Registered succesfuly')
            import databases
        root.destroy()

x = Register(root)
root.mainloop()


