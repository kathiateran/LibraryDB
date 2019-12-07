from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("450x750")

#MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
#print(mydb)

my_cursor = mydb.cursor()

#Database Submissions
def add_book():
    sql_command =""
    values = ""
    my_cursor.execute(sql_command, values)

    mydb.commit()


#TKINTER
title_label = Label(root, text="Administrative Menu", font=("Helvetica", 20))
title_label.grid(row=1, column=0, columnspan=2, pady="12")

#Book Search Form
title_label = Label(root, text="Search Book", font=("Helvetica", 17))
title_label.grid(row=2, column=0, columnspan=2, pady="12")

book_id_label = Label(root,text="Book ISBN").grid(row=3, column=0, sticky=W, padx=10)
book_title_label = Label(root,text="Title").grid(row=4, column=0, sticky=W, padx=10)
book_publisher_label = Label(root,text="Publisher").grid(row=5, column=0, sticky=W, padx=10)

#Entry Boxes
book_id_box = Entry(root)
book_id_box.grid(row=3, column=1, pady=5)

book_title_box = Entry(root)
book_title_box.grid(row=4, column=1, pady=5)

book_publisher_box = Entry(root)
book_publisher_box.grid(row=5, column=1, pady=5)

#Search Button
book_search_button = Button(root, text="Search")
book_search_button.grid(row=6, column=1, padx=5, pady=10)

#Book Actions
title_label = Label(root, text="Add Book Copy", font=("Helvetica", 17))
title_label.grid(row=8, column=0, columnspan=2, pady="12")

book_id_label = Label(root, text="Book ID", font=("Helvetica", 16))
book_id_label.grid(row=9, column=0, columnspan=2, sticky=W, padx=10)

book_id_box = Entry(root)
book_id_box.grid(row=9, column=1, pady=10)

#Action Button
book_add_button = Button(root, text="Add", command=add_book)
book_add_button.grid(row=10, column=1, padx=10, pady=10)

#Reader Actions
title_label = Label(root, text="Add New Reader", font=("Helvetica", 17))
title_label.grid(row=11, column=0, columnspan=2, pady="10")

reader_name_label = Label(root, text="Name", font=("Helvetica", 16))
reader_name_label.grid(row=12, column=0, columnspan=2, sticky=W, padx=10)

reader_id_label = Label(root, text="ID", font=("Helvetica", 16))
reader_id_label.grid(row=13, column=0, columnspan=2, sticky=W, padx=10)

reader_address_label = Label(root, text="Address", font=("Helvetica", 16))
reader_address_label.grid(row=14, column=0, columnspan=2, sticky=W, padx=10)

reader_phone_label = Label(root, text="Phone #", font=("Helvetica", 16))
reader_phone_label.grid(row=15, column=0, columnspan=2, sticky=W, padx=10)

#Entry boxes
reader_name_box = Entry(root)
reader_name_box.grid(row=12, column=1, pady=5)

reader_id_box = Entry(root)
reader_id_box.grid(row=13, column=1, pady=5)

reader_address_box = Entry(root)
reader_address_box.grid(row=14, column=1, pady=5)

reader_phone_box = Entry(root)
reader_phone_box.grid(row=15, column=1, pady=5)

#Button
book_add_button = Button(root, text="Add")
book_add_button.grid(row=16, column=1, padx=10, pady=10)



root.mainloop()