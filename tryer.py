import mysql.connector



mydb = mysql.connector.connect(host='sql4.freesqldatabase.com', password = 'siSVLIJkL8', user = 'sql4423111', database = 'sql4423111', auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute('ALTER TABLE next_of_keen ADD FOREIGN KEY (ID_number) references registry(ID_number')

#mycursor.execute('CREATE TABLE next_of_keen (ID INT NOT NULL, name VARCHAR(255) NOT NULL, phone_number INT NOT NULL PRIMARY KEY, FOREIGN KEY (ID) REFERENCES register(ID) ON UPDATE CASCADE ON DELETE CASCADE)')

#mycursor.execute('CREATE TABLE register (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, phone_number INT NOT NULL, PRIMARY KEY(ID), CONSTRAINT PW_register UNIQUE(password,phone_number))')

#mycursor.execute('DROP TABLE registry')
#mycursor.execute('DROP TABLE keen')

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)

#for x in mycursor:
    #print(x)

#xy = mycursor.execute('Select * from Login')

#for i in mycursor:
    #print(i)
