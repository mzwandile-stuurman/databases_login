from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4423111", password="siSVLIJkL8", database="sql4423111", auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()


root = Tk()
root.title("Logout page Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')

name_label = Label(root, text = "Enter your name:")
name_label.place(x=20,y=50)
name_entry = Entry(root)
name_entry.place(x=200,y=50)

password_label = Label(root, text = "Enter password:")
password_label.place(x=20,y=100)
password_entry = Entry(root)
password_entry.place(x=200,y=100)


def logout():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    sql = "UPDATE logins SET logout = %s WHERE name = %s AND password = %s"
    val = (formatted_date,name_entry.get(), password_entry.get())
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo(title=None, message="Logged Out successfully")
    import main_page
    root.destroy()

logout_btn = Button(root, text = 'Logout', command= logout)
logout_btn.place(x=50,y=150)
root.mainloop()




