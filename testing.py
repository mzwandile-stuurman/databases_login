import mysql.connector

mydb = mysql.connector.connect(host='localhost', password ='@Lifechoices1234', user = 'lifechoices', database = 'mydb', auth_plugin = 'mysql_native_password')
mycursor = mydb.cursor()

#mycursor.execute('ALTER TABLE next_of_keen ADD FOREIGN KEY (ID_number) references registry(ID_number')

#mycursor.execute('CREATE TABLE next_of_keen (ID INT NOT NULL AUTO_INCREMENT, keen_name VARCHAR(255) NOT NULL, keen_number INT NOT NULL PRIMARY KEY, FOREIGN KEY (ID) REFERENCES register(ID) ON UPDATE CASCADE ON DELETE CASCADE)')

#mycursor.execute('CREATE TABLE register (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, phone_number INT NOT NULL, PRIMARY KEY(ID))')

#mycursor.execute('CREATE TABLE logins (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, login VARCHAR(255) NOT NULL,logout VARCHAR(255) DEFAULT NULL,PRIMARY KEY(ID))')

#mycursor.execute('CREATE TABLE admin_reg (ID INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, surname VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, PRIMARY KEY(ID), CONSTRAINT pw_logins UNIQUE(password))')
sql = "INSERT INTO admin_reg (name, surname, password) VALUES (%s, %s, %s)"
val = ("Thapelo", "Tsotetsi", "admin2")
mycursor.execute(sql, val)
mydb.commit()

#mycursor.execute('SELECT register.ID, register.name, register.surname, register.password, register.phone_number,next_of_keen.ID, next_of_keen.keen_name, next_of_keen.keen_number FROM register JOIN next_of_keen ON register.ID = next_of_keen.ID')
#print("ID    Name    Surname    password    phone_number    keen_name    keen_number")
#for row in mycursor:
        #print("%d    %s    %d    %d    %s    %s    %s"%(row[0], row[1],row[2],row[3],row[4],row[5],row[6]))

#mycursor.execute('SHOW TABLES')
#mycursor.execute('DROP TABLE logins')

#mycursor.execute('SELECT * FROM logins')

#for x in mycursor:
    #print(x)

#for x in mycursor:
    #print(x)

#xy = mycursor.execute('Select * from Login')

#for i in mycursor:
    #print(i)
