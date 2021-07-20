from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("600x600")
root.config(bg = "dark slate grey")


user_reg_label = Label(root, text = 'Enter next of kin name:')
user_reg_label.place(x= 20, y= 50)
user_reg_entry = Entry(root)
user_reg_entry.place(x = 200, y = 50)

pass_reg_label = Label(root, text = 'Enter next of kin cell number:')
pass_reg_label.place(x = 20 , y = 150)
pass_reg_entry = Entry(root)
pass_reg_entry.place(x = 220 , y = 150)



# insert next of keen to details to next of keen table
def reg():
    if pass_reg_entry.get() == "" or user_reg_entry.get() == "":
        messagebox.showwarning(title='Invalid', message='Please enter valid details.')
    elif pass_reg_entry.get() == " " or user_reg_entry.get() == " ":
        messagebox.showwarning(title="Space", message="Please enter valid details.")
    elif len(pass_reg_entry.get())>10:
        messagebox.showinfo(title="Wrong Number", message="Please enter correct number")

    else:

        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
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


