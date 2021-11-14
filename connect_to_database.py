#Import the neccesary modules to connect to a postgresql database
import psycopg2
# connect to the database
try:
    connection = psycopg2.connect(database="staff", user="alistair", password="python", host="127.0.0.1", port="5432")
# print a message if there is a error while connecting
except psycopg2.Error as err:
    print("An error was generated!")
#display this message if the connection  is successful
else:
    print("Connection to database was successful!")