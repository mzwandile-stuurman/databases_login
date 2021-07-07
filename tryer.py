import mysql.connector

mydb = mysql.connector.connect(host='sql4.freesqldatabase.com', password = 'siSVLIJkL8', user = 'sql4423111', database = 'sql4423111', auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute('ALTER TABLE next_of_keen ADD FOREIGN KEY (ID_number) references registry(ID_number')

#mycursor.execute('CREATE TABLE next_of_keen (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, phone_number INT NOT NULL PRIMARY KEY, FOREIGN KEY (ID) REFERENCES register(ID) ON UPDATE CASCADE ON DELETE CASCADE)')

#mycursor.execute('CREATE TABLE register (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, phone_number INT NOT NULL, PRIMARY KEY(ID), CONSTRAINT PW_register UNIQUE(password,phone_number))')

#mycursor.execute('CREATE TABLE logins (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, login VARCHAR(255) NOT NULL,logout VARCHAR(255) NOT NULL ,PRIMARY KEY(ID), CONSTRAINT pw_logins UNIQUE(password))')

#mycursor.execute('CREATE TABLE admin_reg (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, PRIMARY KEY(ID), CONSTRAINT pw_logins UNIQUE(password))')
#sql = "INSERT INTO admin_reg (name, surname, password) VALUES (%s, %s, %s)"
#val = ("Thapelo", "Tsotetsi", "admin2")
#mycursor.execute(sql, val)
#mydb.commit()


#mycursor.execute('SHOW TABLES')
#mycursor.execute('DROP TABLE keen')

mycursor.execute('SELECT * FROM admin_reg')

for x in mycursor:
    print(x)

#for x in mycursor:
    #print(x)

#xy = mycursor.execute('Select * from Login')

#for i in mycursor:
    #print(i)
