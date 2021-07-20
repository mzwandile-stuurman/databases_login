from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')

root = Tk()
root.title("Login Page")
root.geometry("1200x1200")
root.config(bg = 'dark slate grey')

# Logins table treeview

trv2 = ttk.Treeview(root, selectmode ='browse')
trv2.grid(row=2,column=1)

trv2["columns"] = ("1", "2", "3","4","5","6")
trv2['show'] = 'headings'

trv2.column("1", width = 30, anchor ='c')
trv2.column("2", width = 100, anchor ='c')
trv2.column("3", width = 100, anchor ='c')
trv2.column("4", width = 100, anchor ='c')
trv2.column("5", width = 180, anchor ='c')
trv2.column("6",width =180, anchor = 'c')



trv2.heading("1", text ="ID")
trv2.heading("2", text ="name")
trv2.heading("3", text ="surname")
trv2.heading("4", text ="password")
trv2.heading("5", text ="login")
trv2.heading("6", text = "logout")

mycursor = mydb.cursor()
xy = mycursor.execute('SELECT * FROM logins')


for dt in mycursor:
    trv2.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))


# Register table treeview
trv = ttk.Treeview(root, selectmode ='browse')
trv.grid(row=1,column=1,pady=40)

trv["columns"] = ("1", "2", "3","4","5","6","7")
trv['show'] = 'headings'

trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 100, anchor ='c')
trv.column("3", width = 100, anchor ='c')
trv.column("4", width = 100, anchor ='c')
trv.column("5", width = 120, anchor ='c')
trv.column("6",width =150, anchor = 'c')
trv.column("7", width = 150, anchor = 'c')


trv.heading("1", text ="ID")
trv.heading("2", text ="name")
trv.heading("3", text ="surname")
trv.heading("4", text ="password")
trv.heading("5", text ="phone_number")
trv.heading("6", text = "keen_name")
trv.heading("7", text = "keen_number")

mycursor = mydb.cursor()
xy = mycursor.execute('SELECT register.ID, register.name, register.surname, register.password, register.phone_number, next_of_keen.keen_name, next_of_keen.keen_number FROM register JOIN next_of_keen ON register.ID = next_of_keen.ID')

for dt in mycursor:
    trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6]))

# add scrollbar to register treeview
scrollbar = ttk.Scrollbar(root, orient = 'vertical', command =trv.yview())
scrollbar.grid(row=1,column=2)
trv.configure(yscrollcommand = scrollbar.set)

var = StringVar()
var2 = StringVar()

registry =Label(root, text='Registered users', bg ='white')
registry.place(x=10,y=10)

login_history = Label(root, text = 'Login History', bg = 'white')
login_history.place(x=100,y=275)

update_frame = Frame(root, width = 300, height = 200)
update_frame.place(x=740,y=300)
update_label = Label(root, text ='Field to update:')
update_label.place(x=750, y=350)
update_entry = Entry(root)
update_entry.place(x=860, y=350)
what_label = Label(root, text = 'Update what: ')
what_label.place(x=750,y=400)
what_entry = Entry(root)
what_entry.place(x=860,y=400)
into_label = Label(root, text= 'update to:')
into_label.place(x=750, y=450)
into_entry = Entry(root)
into_entry.place(x=860,y=450)

# checking users who signed in
update_headig = Label(root,text='Update a field', bg = 'white', width= 25)
update_headig.place(x=780,y=315)
people_loged_in = Label(root, text = 'logged in:')
people_loged_in.place(x=890,y=10)
number = Label(root, text = '',textvariable = var, bg='white', width = 3)
number.place(x=960,y=10)

mycursor.execute('SELECT COUNT(DISTINCT login) FROM logins')
for i in mycursor:
        var.set(i[0])

#checking users who have signed out
people_logged_out = Label(root, text='Logged out:')
people_logged_out.place(x=1000,y=10)
number_out = Label(root, text='', textvariable = var2, bg='white', width=3)
number_out.place(x=1090,y=10)
mycursor.execute('SELECT COUNT(DISTINCT logout) FROM logins')
for x in mycursor:
        var2.set(x[0])


# Delete selected user from register tree view
def delete():

    selected = trv.focus()
    values = trv.item(selected,'values')
    if selected == "":
        messagebox.showwarning(title="wrong table", message='Select "Registered users" table')

    else:

        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "DELETE FROM register WHERE id = %s"
        val = (values[0],)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Deleted', message='Record deleted.')
    trv.delete(selected)

# update selected entry from register tree view
def update():

    if update_entry.get() == 'name':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET name = %s WHERE name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes.')

    elif update_entry.get() == 'surname':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET surname = %s WHERE surname = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes.')

    elif update_entry.get() == 'password':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET password = %s WHERE password = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes. ')

    elif update_entry.get() == 'phone_number':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE register SET phone_number = %s WHERE phone_number= %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes.')

    elif update_entry.get() == 'keen_name':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_keen SET keen_name = %s WHERE keen_name = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes. ')

    elif update_entry.get() == 'keen_number':
        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE next_of_keen SET keen_number = %s WHERE keen_number = %s"
        val = (into_entry.get(),what_entry.get())
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Updated', message='Field updated successfully. Restart to see changes. ')

    else:
        if update_entry.get() == "":
            messagebox.showwarning(title='NUll', message='Please enter correct record')

# add user to admin
def add_admin():
    selected = trv.focus()
    values = trv.item(selected,'values')
    mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO admin_reg (name, surname, password) VALUES (%s, %s , %s)"
    val = (values[1],values[2],values[3],)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo(title='Added', message='User is now admin. Restart to see chages.')

# logout user as admin
def logout_user():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    selected = trv2.focus()
    values = trv2.item(selected,'values')
    if selected == '':
        messagebox.showinfo(title="Null", message='Please select a record from "Login History"')

    else:

        mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
        mycursor = mydb.cursor()
        sql = "UPDATE logins SET logout = %s WHERE ID = %s AND password = %s"
        val = (formatted_date,values[0],values[3],)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo(title='Logged Out', message='User is now logged out.')

# view admin table
def view_admin():

    trv2 = ttk.Treeview(root, selectmode ='browse')
    trv2.grid(row=3,column=1,padx=20,pady=20)

    trv2["columns"] = ("1", "2", "3","4")
    trv2['show'] = 'headings'

    trv2.column("1", width = 30, anchor ='c')
    trv2.column("2", width = 100, anchor ='c')
    trv2.column("3", width = 100, anchor ='c')
    trv2.column("4", width = 100, anchor ='c')

    trv2.heading("1", text ="ID")
    trv2.heading("2", text ="name")
    trv2.heading("3", text ="surname")
    trv2.heading("4", text ="password")


    mycursor = mydb.cursor()
    xy = mycursor.execute('SELECT * FROM admin_reg')


    for dt in mycursor:
        trv2.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3]))

# add new record as an admin

def add_record():
    root.destroy()
    import register

# exit admin and go back to main page
def exit():
    root.destroy()
    import main_page

delete_btn = Button(root, text = 'Delete selected row', command = delete)
delete_btn.place(x=850,y=50)

update_btn = Button(root, text = 'Update', command = update)
update_btn.place(x=870,y=505)

add_btn = Button(root, text = 'Add new user')
add_btn.place(x=850, y=150)

add_adim_btn = Button(root, text = 'Add user as Admin')
add_adim_btn.place(x=980,y=150)

logout_btn = Button(root, text = 'Logout user', command = logout_user)
logout_btn.place(x=850,y=200)

exit_btn = Button(root, text = 'Go to main page', command = exit)
exit_btn.place(x=850, y=250)

view_admin_btn = Button(root, text = 'View Admin users', command = view_admin)
view_admin_btn.place(x=850,y=100)


root.mainloop()
