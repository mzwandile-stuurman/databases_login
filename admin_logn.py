from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

root = Tk()
root.title("Login Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')


name_label = Label(root, text = "Enter your name:")
name_label.place(x=20,y=50)
name_entry = Entry(root)
name_entry.place(x=200,y=50)

surname_label = Label(root, text = "Enter your surname")
surname_label.place(x=20, y = 100)
surname_entry = Entry(root)
surname_entry.place(x=200,y=100)

password_label = Label(root, text = "Enter admin password:")
password_label.place(x=20, y=150)
password_entry = Entry(root)
password_entry.place(x=200, y=150)




def password():

    mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'Project', auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from admin_reg')

    found = False
    for i in mycursor:
        if i[3] == password_entry.get():
            found = True
    if found == True:
        messagebox.showinfo(title="Accepted", message="Login Accepted.")
        root.destroy()
        import admin_main

    else:
        messagebox.showwarning(title="Stop",message="Your not admin / Incorrect details")
        root.destroy()
        import main_page


login_btn = Button(root, text = "Login", command = password)
login_btn.place(x=50, y=200)
root.mainloop()





