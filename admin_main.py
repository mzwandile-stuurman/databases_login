from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')

root = Tk()
root.title("Login Page")
root.geometry("600x600")
root.config(bg = 'dark slate grey')

trv = ttk.Treeview(root, selectmode ='browse')
trv.grid(row=1,column=1,padx=20,pady=20)

trv["columns"] = ("1", "2", "3","4","5")
trv['show'] = 'headings'

trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 100, anchor ='c')
trv.column("3", width = 100, anchor ='c')
trv.column("4", width = 100, anchor ='c')
trv.column("5", width = 120, anchor ='c')


trv.heading("1", text ="ID")
trv.heading("2", text ="name")
trv.heading("3", text ="surname")
trv.heading("4", text ="password")
trv.heading("5", text ="phone_number")

mycursor = mydb.cursor()
xy = mycursor.execute('Select * from register')

for dt in mycursor:
    trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4]))

def delete():

    selected = trv.focus()
    values = trv.item(selected,'values')
    mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    sql = "DELETE FROM register WHERE id = %s"
    val = (values[0],)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo(title='Deleted', message='Record deleted.')


def update():
    update_label = Label(root, text ='Field to update:')
    update_label.place(x=40, y=350)
    update_entry = Entry(root)
    update_entry.place(x=100, y=350)
    what_label = Label(root, text = 'Update: ')
    what_label.place(x=40,y=450)
    what_entry = Entry(root)
    what_entry.place(x=100,y=450)
    into_label = Label(root, text= 'update to:')
    into_label.place(x=40, y=550)
    into_entry = Entry(root)
    into_entry.place(x=40,y=550)

    if update_entry.get() == 'name':
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET name = %s WHERE name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
    elif update_entry.get() == 'surname':

        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET surname = %s WHERE surname = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'password':
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET password = %s WHERE password = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'phone_number':
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET phone_number = %s WHERE phone_number= %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'keen_name':
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_keen SET keen_name = %s WHERE keen_name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    elif update_entry.get() == 'keen_number':
        mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_keen SET keen_number = %s WHERE keen_number = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()

    else:
        messagebox.showwarning(title='NUll', message='Please enter correct record')





def add_record():
    root.destroy()
    import register

delete_btn = Button(root, text = 'Delete selected row', command = delete)
delete_btn.place(x=20,y=300)

update_btn = Button(root, text = 'Update a record', command = update)
update_btn.place(x=20,y=300)





root.mainloop()
