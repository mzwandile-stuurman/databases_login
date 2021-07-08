from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("300x300")
root.config(bg = "dark slate grey")



user_reg_label = Label(root, text = 'Enter next of kin name:')
user_reg_label.place(x= 20, y= 50)
user_reg_entry = Entry(root)
user_reg_entry.place(x = 100, y = 50)

pass_reg_label = Label(root, text = 'Enter next of kin cell number:')
pass_reg_label.place(x = 20 , y = 150)
pass_reg_entry = Entry(root)
pass_reg_entry.place(x = 100 , y = 150)




def reg():
    if pass_reg_entry.get() == None or user_reg_entry.get() == None:
        messagebox.showwarning(title='Invalid', message='Please enter valid details.')
    elif pass_reg_entry.get() == " " or user_reg_entry.get() == " ":
        messagebox.showwarning(title="Space", message="Please enter valid details.")

    else:

        mydb = mysql.connector.connect(host="sql4.freesqldatabase.com", user="sql4423111", password="siSVLIJkL8", database="sql4423111", auth_plugin = 'mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO next_of_keen (keen_name, keen_number) VALUES ( %s, %s)"
        val = (user_reg_entry.get(), pass_reg_entry.get())
        mycursor.execute(sql, val)

        mydb.commit()
        messagebox.showinfo(title="Success", message='Registered succesfuly-Login.')

        root.destroy()
        import main_page

reg_btn = Button(root, text = "Register", command = reg)
reg_btn.place(x= 50, y=250)

root.mainloop()


