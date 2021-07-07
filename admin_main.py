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




root.mainloop()
