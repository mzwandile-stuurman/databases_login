from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("Login Page")
root.geometry("300x300")
root.config(bg = 'dark slate grey')

class Login:
    def __init__(self,master):
        self.user_label = Label(master, text = "Enter your name:")
        self.user_label.place(x=20,y=50)
        self.user_entry = Entry(master)
        self.user_entry.place(x=100,y=50)

        self.password_label = Label(master, text = "Please enter password:")
        self.password_label.place(x=20, y=100)
        self.password_entry = Entry(master)
        self.password_entry.place(x=100, y=100)

        self.login_btn = Button(master, text = "Login", command = self.password)
        self.login_btn.place(x=50, y=150)

        self.reg_btn = Button(master, text = 'Register')
        self.reg_btn.place(x= 50, y=200)




    def password(self):
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from register')

        for i in mycursor:

            if i[0] == self.user_entry.get() and i[1] == self.password_entry.get():
                messagebox.showinfo(title="Correct", message="Login Accepted")

                sql = "INSERT INTO logins (name, surname, password) VALUES (%s, %s, %s,%s)"
                val = (self.user_entry.get(), self.password_entry.get())
                mycursor.execute(sql, val)
                mydb.commit()

        if i[0] != self.user_entry.get() or i[1] != self.password_entry.get():
                messagebox.showwarning(title="Incorrect", message="Login Denied")
                self.user_entry.delete(0,END)
                self.password_entry.delete(0,END)

x = Login(root)

root.mainloop()

