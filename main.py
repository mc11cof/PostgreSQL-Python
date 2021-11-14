# Import module for postgresql
import psycopg2

#File containing data
f = open("C:\\Users\\marca\\Documents\\Automate_Database\\employees.txt")

#Make a empty list
records = []

for i in f.readlines():
    records.append(i.split("/ "))

try:
    connection = psycopg2.connect(database="staff", user="alistair", password="python", host="127.0.0.1", port="5432")
# print a message if there is a error while connecting
except psycopg2.Error as err:
    print("An error was generated while connecting to the database  !")
#display this message if   the connection  is successful
else:
    print("Connection to database was successful!\n")

cursor = connection.cursor()

# Iterating over the records list and, for each inner list, extracting the data associated with each of the 7 columns in the table using indexes and inserting the data in the table using the INSERT command
try:
    for i in records:
        cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) values (%s,%s,%s,%s,%s,%s,%s);", (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

except psycopg2.Error as err:
    print("An error was generated while inserting the records!")

else:
    print("Records inserted successfully!\n")

# Committing (saving) the changes to the database
connection.commit()

# Closing the connection to the database
connection.close()

#This is the end of the program
