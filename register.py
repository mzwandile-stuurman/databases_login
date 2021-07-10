from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("450x450")
root.config(bg = "dark slate grey")



name_reg_label = Label(root, text = 'Enter name:')
name_reg_label.place(x= 20, y= 50)
name_reg_entry = Entry(root)
name_reg_entry.place(x = 150, y = 50)

surname_reg_label = Label(root, text = 'Enter surname:')
surname_reg_label.place(x = 20 , y = 100)
surname_reg_entry = Entry(root)
surname_reg_entry.place(x = 150 , y = 100)

password_label = Label(root, text = 'Create password: ')
password_label.place(x=20 , y = 150)
password_entry = Entry(root)
password_entry.place(x=150 , y= 150)

cell_number_label = Label(root, text = 'Enter cell number')
cell_number_label.place(x= 20 , y = 200)
cell_number_entry = Entry(root)
cell_number_entry.place(x=150, y=200)



def reg():

    if name_reg_entry.get() == "" or surname_reg_entry.get() == "" or password_entry.get() == "" or cell_number_entry.get() == "":
        messagebox.showwarning(title='Invalid', message='Please enter valid details.')
    elif name_reg_entry.get() == " " or surname_reg_entry.get() == " " or password_entry == " " or cell_number_entry == " ":
        messagebox.showwarning(title="Space", message="Please enter valid details.")
    elif len(cell_number_entry.get())>10:
        messagebox.showinfo(title='Incorrect number', message='Please enter a correct number!')
        name_reg_entry.delete(0,END)
        surname_reg_entry.delete(0,END)
        password_entry.delete(0,END)
        cell_number_entry.get(0,END)

    else:

        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'Project', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()

        sql = "INSERT INTO register (name, surname, password, phone_number) VALUES (%s, %s, %s, %s)"
        val = (name_reg_entry.get(), surname_reg_entry.get(),password_entry.get(),cell_number_entry.get())
        mycursor.execute(sql, val)

        mydb.commit()
        #messagebox.showinfo(title="Valid", message='Please enter next of keen.')
        root.destroy()
        import keen_details

reg_btn = Button(root, text = "Enter next of keen details", command = reg)
reg_btn.place(x= 50, y=350)


root.mainloop()


