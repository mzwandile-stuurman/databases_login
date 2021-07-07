from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime


root = Tk()
root.title("Logout page Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')

class Logout():
    def __init__(self,master):
        self.name_label = Label(master, text = "Enter your name:")
        self.name_label.place(x=20,y=50)
        self.name_entry = Entry(master)
        self.name_entry.place(x=200,y=50)

        self.password_label = Label(master, text = "Enter password:")
        self.password_label.place(x=20,y=100)
        self.password_entry = Entry(master)
        self.password_entry.place(x=200,y=100)

        self.logout_btn = Button(master, text = 'Logout', command= self.logout)
        self.logout_btn.place(x=50,y=150)

    def logout(self):
        self.now = datetime.now()
        self.formatted_date = self.now.strftime('%Y-%m-%d %H:%M:%S')
        mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4423111", password="siSVLIJkL8", database="sql4423111", auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()

        sql = "UPDATE logins SET logout = %s WHERE password = %s"
        val = (self.formatted_date,self.password_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title=None, message="Logged Out successfully")
        import main_page
        root.destroy()

x= Logout(root)
root.mainloop()




