# Mzwandile Stuurman

# Importing Modules
from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime


root = Tk()
root.title("Login Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')

# Creating Entries and labels
now = datetime.now()
formatted_date =now.strftime('%Y-%m-%d %H:%M:%S')
name_label = Label(root, text = "Enter your name:")
name_label.place(x=20,y=50)
name_entry = Entry(root)
name_entry.place(x=200,y=50)

surname_label = Label(root, text = "Enter your surname")
surname_label.place(x=20, y = 100)
surname_entry = Entry(root)
surname_entry.place(x=200,y=100)

password_label = Label(root, text = "Please enter password:")
password_label.place(x=20, y=150)
password_entry = Entry(root)
password_entry.place(x=200, y=150)


# This function insert user to Logins table if password is correct
def password():

    mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from register')
    found = False

    for i in mycursor:
        if i[3] == password_entry.get():
            found = True

    if found == True:

        messagebox.showinfo(title="Correct", message="Login Accepted")

        mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4423111", password="siSVLIJkL8", database="sql4423111", auth_plugin = 'mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO logins (name, surname, password,login) VALUES (%s, %s, %s,%s)"
        val = (name_entry.get(),surname_entry.get(),password_entry.get(),formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()
        root.withdraw()
        import logout_page

    else:

        messagebox.showwarning(title="Incorrect", message="Login Denied - Register")
        name_entry.delete(0,END)
        password_entry.delete(0,END)
        surname_entry.delete(0,END)

# This function takes user to admin screen
def admin():

    root.destroy()
    import admin_logn

# This functions takes user to the register screen
def reg():
    root.destroy()
    import register



login_btn = Button(root, text = "Login", command =password)
login_btn.place(x=50, y=200)

reg_btn = Button(root, text = 'Register', command =reg)
reg_btn.place(x= 150, y=200)

admin_btn = Button(root, text = 'Login as Admin', command =admin)
admin_btn.place(x=300,y=200)



root.mainloop()

