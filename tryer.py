import mysql.connector
import MySQLdb


mydb = mysql.connector.connect(user='sql4423111', password = 'siSVLIJkL8', host = 'sql4.freesqldatabase.com', database = 'sql4423111', auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE next_of_keen (ID_number INT NOT NULL, name VARCHAR(255) NOT NULL, phone_number INT NOT NULL),PRIMARY KEY(phone_number) FOREIGN KEY(ID_number) REFERENCES registry(ID_number)')
#mycursor.execute('DROP TABLE registry')

#for x in mycursor:
    #print(x)

#xy = mycursor.execute('Select * from Login')

#for i in mycursor:
    #print(i)
