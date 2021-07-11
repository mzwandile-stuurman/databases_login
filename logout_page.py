from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'Project', auth_plugin = 'mysql_native_password')
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


# submit logout information
def exit():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    sql = "UPDATE logins SET logout = %s WHERE name = %s AND password = %s"
    val = (formatted_date,name_entry.get(), password_entry.get())
    mycursor.execute(sql,val)
    mydb.commit()
    name_entry.delete(0,END)
    password_entry.delete(0,END)
    messagebox.showinfo(title=None, message="Logged Out successfully. Please login the next user. Thank you")
def back_to_main():
    root.destroy()
    import main_page

logout_btn = Button(root, text = 'Submit', command= exit)
logout_btn.place(x=50,y=150)

main_screen_btn= Button(root, text = 'Go to main screen', command=back_to_main)
main_screen_btn.place(x=50,y=200)
root.mainloop()




