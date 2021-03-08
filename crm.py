import psycopg2
from tkinter import *
root=Tk()
root.title('CRM System')
root.geometry("600x600")

DB_NAME = "customerreldatabase" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "root"

conn = psycopg2.connect(database=DB_NAME,user=DB_USER,host=DB_HOST,port=DB_PORT,password=DB_PASS)
print('database connected')
my_cursor=conn.cursor()
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	zipcode INT,
	price_paid DECIMAL(10,2),
	user_id SERIAL PRIMARY KEY,
	email VARCHAR(255),
	address_1 VARCHAR(255),
	address_2 VARCHAR(255),
	city VARCHAR(50),
	state VARCHAR(50),
	country VARCHAR(255),
	phone VARCHAR(255),
	payment_method VARCHAR(50),
	discount_code VARCHAR(255)
	)""")
conn.commit()



#alter the table
# my_cursor.execute("ALTER TABLE customers(\
# 	ADD COLUMN email VARCHAR(255))")
# conn.commit()
#check table description
# my_cursor.execute("SELECT * FROM customers")
# print(my_cursor.description)

#clear text fields function
def clear_fields():
	first_name_box.delete(0,END)
	last_name_box.delete(0,END)
	zipcode_box.delete(0,END)
	price_paid_box.delete(0,END)
	email_box.delete(0,END)
	address_1_box.delete(0,END)
	address_2_box.delete(0,END)
	city_box.delete(0,END)
	state_box.delete(0,END)
	country_box.delete(0,END)
	phone_box.delete(0,END)
	payment_method_box.delete(0,END)
	discount_code_box.delete(0,END)

	
def add_customer():
	sql_command = "INSERT INTO customers (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	values = (first_name_box.get(),last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(),address_1_box.get(),address_2_box.get(),city_box.get(),state_box.get(),country_box.get(),phone_box.get(),payment_method_box.get(),discount_code_box.get())
	my_cursor.execute(sql_command,values)
	conn.commit()

	# clear fields when click button
	clear_fields()

#create a label
title_label = Label(root,text="Customer Database", font=('Helvetica',16))
title_label.grid(row=0,column=0,pady="10")

# Create main form to enter customer data
first_name_label=Label(root,text='First Name').grid(row=1,column=0,sticky=W,padx=10)
last_name_label=Label(root,text='Last_Name').grid(row=2,column=0,sticky=W,padx=10)
zipcode_label=Label(root,text='ZipCode').grid(row=3,column=0,sticky=W,padx=10)
price_paid_label=Label(root,text='Price Paid').grid(row=4,column=0,sticky=W,padx=10)
email_label=Label(root,text='Email').grid(row=5,column=0,sticky=W,padx=10)
address_1_label=Label(root,text='Address One').grid(row=6,column=0,sticky=W,padx=10)
address_2_label=Label(root,text='Address Two').grid(row=7,column=0,sticky=W,padx=10)
city_label=Label(root,text='City').grid(row=8,column=0,sticky=W,padx=10)
state_label=Label(root,text='State').grid(row=9,column=0,sticky=W,padx=10)
country_label=Label(root,text='Country').grid(row=10,column=0,sticky=W,padx=10)
phone_label=Label(root,text='Phone').grid(row=11,column=0,sticky=W,padx=10)
payment_method_label=Label(root,text='Payment Method').grid(row=12,column=0,sticky=W,padx=10)
discount_code_label=Label(root,text='Discount Code').grid(row=13,column=0,sticky=W,padx=10)


#Create Entry Boxes

first_name_box=Entry(root)
first_name_box.grid(row=1,column=1)

last_name_box=Entry(root)
last_name_box.grid(row=2,column=1,pady=5)

zipcode_box=Entry(root)
zipcode_box.grid(row=3,column=1,pady=5)

price_paid_box=Entry(root)
price_paid_box.grid(row=4,column=1,pady=5)

email_box=Entry(root)
email_box.grid(row=5,column=1,pady=5)

address_1_box=Entry(root)
address_1_box.grid(row=6,column=1,pady=5)

address_2_box=Entry(root)
address_2_box.grid(row=7,column=1,pady=5)

city_box=Entry(root)
city_box.grid(row=8,column=1,pady=5)

state_box=Entry(root)
state_box.grid(row=9,column=1,pady=5)

country_box=Entry(root)
country_box.grid(row=10,column=1,pady=5)

phone_box=Entry(root)
phone_box.grid(row=11,column=1,pady=5)

payment_method_box=Entry(root)
payment_method_box.grid(row=12,column=1,pady=5)

discount_code_box=Entry(root)
discount_code_box.grid(row=13,column=1,pady=5)


#create Buttons
add_customer_button=Button(root,text='Add Customer',command=add_customer)
add_customer_button.grid(row=14,column=0,padx=10,pady=10)

clear_fields_button=Button(root,text='Clear Fields',command=clear_fields)
clear_fields_button.grid(row=14,column=1,padx=10,pady=10)

root.mainloop()