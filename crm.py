import psycopg2
from tkinter import *
root=Tk()
root.title('CRM System')
root.geometry("400x400")

DB_NAME = "customerreldatabase" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "root"

conn = psycopg2.connect(database=DB_NAME,user=DB_USER,host=DB_HOST,port=DB_PORT,password=DB_PASS)
print('database connected')
my_cursor=conn.cursor()
# my_cursor.execute("""CREATE TABLE customers(
# 	first_name VARCHAR(255),
# 	last_name VARCHAR(255),
# 	zipcode INT,
# 	price_paid DECIMAL(10,2),
# 	user_id SERIAL PRIMARY KEY
# 	)""")
# conn.commit()



#alter the table
my_cursor.execute("ALTER TABLE customers(\
	ADD COLUMN email VARCHAR(255))")
conn.commit()
#check table description
# my_cursor.execute("SELECT * FROM customers")
# print(my_cursor.description)
root.mainloop()