from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("325x450")

#MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
#print(mydb)

my_cursor = mydb.cursor()

#DATABASE
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
    #print(db)

#TABLES
#library Branch
#my_cursor.execute("CREATE TABLE library_branch(lib_id INTEGER(10), branch_name VARCHAR(155), branch_location VARCHAR(255))")

#Book --> have to figure out how to have composite primary key
#my_cursor.execute("CREATE TABLE book_data(ISBN INTEGER AUTO_INCREMENT PRIMARY KEY, \
 #   copy_no INTEGER(10), \
  #  title VARCHAR(255), book_branch VARCHAR(155), \
  #  book_publisher VARCHAR(155), book_reader VARCHAR(155), \
   # book_author VARCHAR(155), publication_date VARCHAR(55))")

#Author
#my_cursor.execute("CREATE TABLE author(author_id INTEGER(10), author_name VARCHAR(155))")

#Publisher
#my_cursor.execute("CREATE TABLE publisher(publisher_id INTEGER(10), publisher_address VARCHAR(255))")

#Reader
#my_cursor.execute("CREATE TABLE reader_data(reader_id INTEGER(10), reader_name VARCHAR(155), \
 #   reader_address VARCHAR(255), phone_no INTEGER(20))")

#def clear_fields():
 #   card_number_box.delete(0, END)
  #  reader_name_box.delete(0, END)
   # admin_id_box.delete(0, END)
    #admin_name_box.delete(0, END)

#TKINTER
title_label = Label(root, text="Main Menu", font=("Helvetica", 20))
title_label.grid(row=1, column=0, columnspan=2, pady="12")

title_label = Label(root, text="Reader Login", font=("Helvetica", 17))
title_label.grid(row=2, column=0, columnspan=2, pady="12")


#READER Login Form
card_number_label = Label(root,text="Card No.").grid(row=3, column=0, sticky=W, padx=10)
reader_name_label = Label(root,text="Name").grid(row=4, column=0, sticky=W, padx=10)

#Entry Boxes
card_number_box = Entry(root)
card_number_box.grid(row=3, column=1, pady=5)

reader_name_box = Entry(root)
reader_name_box.grid(row=4, column=1)

#ADMIN Login Form
title_label = Label(root, text="\nAdministrative Login", font=("Helvetica", 17))
title_label.grid(row=7, column=0, columnspan=2, pady="12")

admin_id_label = Label(root,text="Admin ID").grid(row=8, column=0, sticky=W, padx=10)
admin_name_label = Label(root,text="Name").grid(row=9, column=0, sticky=W, padx=10)

#Entry Boxes
admin_id_box = Entry(root)
admin_id_box.grid(row=8, column=1, pady=5)

admin_name_box = Entry(root)
admin_name_box.grid(row=9, column=1, pady=10)

#Login Buttons
reader_login_button = Button(root, text="Login")
reader_login_button.grid(row=5, column=1, padx=5, pady=10)

admin_login_button = Button(root, text="Login")
admin_login_button.grid(row=10, column=1, padx=5, pady=10)



root.mainloop()