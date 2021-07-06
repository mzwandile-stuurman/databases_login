from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime


root = Tk()
root.title("Login Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')

class Login:
    def __init__(self,master):
        self.now = datetime.now()
        self.formatted_date = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.name_label = Label(master, text = "Enter your name:")
        self.name_label.place(x=20,y=50)
        self.name_entry = Entry(master)
        self.name_entry.place(x=200,y=50)

        self.surname_label = Label(master, text = "Enter your surname")
        self.surname_label.place(x=20, y = 100)
        self.surname_entry = Entry(master)
        self.surname_entry.place(x=200,y=100)

        self.password_label = Label(master, text = "Please enter password:")
        self.password_label.place(x=20, y=150)
        self.password_entry = Entry(master)
        self.password_entry.place(x=200, y=150)

        self.login_btn = Button(master, text = "Login", command = self.password)
        self.login_btn.place(x=50, y=200)

        self.reg_btn = Button(master, text = 'Register')
        self.reg_btn.place(x= 150, y=200)





    def password(self):

        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        xy = mycursor.execute('Select * from register')

        for i in mycursor:

            if i[3] == self.password_entry.get():
                messagebox.showinfo(title="Correct", message="Login Accepted")

                mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4423111", password="siSVLIJkL8", database="sql4423111", auth_plugin = 'mysql_native_password')

                mycursor = mydb.cursor()

                sql = "INSERT INTO logins (name, surname, password,date) VALUES (%s, %s, %s,%s)"
                val = (self.name_entry.get(), self.surname_entry.get(), self.password_entry.get(),self.formatted_date)
                mycursor.execute(sql, val)
                mydb.commit()

            elif i[3] != self.password_entry.get():

                messagebox.showwarning(title="Incorrect", message="Login Denied")
                self.name_entry.delete(0,END)
                self.password_entry.delete(0,END)

x = Login(root)

root.mainloop()

