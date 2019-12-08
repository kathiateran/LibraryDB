from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("750x850")

#MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
#print(mydb)

my_cursor = mydb.cursor()

def clear_fields():
    book_id_box.delete(0, END)
    copy_no_box.delete(0, END)
    book_title_box.delete(0, END)
    book_branch_box.delete(0, END)
    book_publisher_box.delete(0, END)
    book_author_box.delete(0, END)
    publication_date_box.delete(0, END)

#Database Submissions
def add_book():
    sql_command = "INSERT INTO book_data(book_id, copy_no, book_title, book_branch, " \
                  "book_publisher, book_author, publication_date) VALUES(%, %, %, %, %, %, %)"
    values = (book_id_box.get(), copy_no_box.get(), book_title_box.get(), book_branch_box.get(),
              book_publisher_box.get(), book_author_box.get(), publication_date_box.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear_fields()


#TKINTER
title_label = Label(root, text="Administrative Menu", font=("Helvetica", 20)).grid(row=1, column=2, pady="12")

#Book Search Form
title_label = Label(root, text="Search Book", font=("Helvetica", 17)).grid(row=2, column=1, pady="12")
book_id_label = Label(root,text="Book ISBN").grid(row=3, column=0, sticky=W, padx=10)
book_title_label = Label(root,text="Title").grid(row=4, column=0, sticky=W, padx=10)
book_publisher_label = Label(root,text="Publisher").grid(row=5, column=0, sticky=W, padx=10)

#Entry Boxes
book_id_box = Entry(root).grid(row=3, column=1, pady=5)
book_title_box = Entry(root).grid(row=4, column=1, pady=5)
book_publisher_box = Entry(root).grid(row=5, column=1, pady=5)

#Search Button
book_search_button = Button(root, text="Search").grid(row=6, column=1, padx=5, pady=10)

#Book Actions
title_label = Label(root, text="Add Book Copy", font=("Helvetica", 17)).grid(row=8, column=2, pady="12")
book_id_label = Label(root, text="ISBN").grid(row=9, column=0, sticky=W, padx=10)
copy_no_label = Label(root, text="Copy No.").grid(row=10, column=0, sticky=W, padx=10)
book_title_label = Label(root, text="Title").grid(row=11, column=0, sticky=W, padx=10)
book_branch_label = Label(root, text="Book Branch").grid(row=12, column=0, sticky=W, padx=10)
book_publisher_label = Label(root, text="Publisher").grid(row=9, column=2, sticky=W, padx=10)
book_author_label = Label(root, text="Author").grid(row=10, column=2, sticky=W, padx=10)
publication_date_label = Label(root, text="Publication Date").grid(row=11, column=2, sticky=W, padx=10)

#Entries
book_id_box = Entry(root).grid(row=9, column=1, pady=10)
copy_no_box = Entry(root).grid(row=10, column=1, pady=10)
book_title_box = Entry(root).grid(row=11, column=1, pady=10)
book_branch_box = Entry(root).grid(row=12, column=1, pady=10)
book_publisher_box = Entry(root).grid(row=9, column=3, pady=10)
book_author_box = Entry(root).grid(row=10, column=3, pady=10)
publication_date_box = Entry(root).grid(row=11, column=3, pady=10)

#Action Button
book_add_button = Button(root, text="ADD", command=add_book).grid(row=12, column=3, padx=10, pady=10)

#Reader Actions
title_label = Label(root, text="Add New Reader", font=("Helvetica", 17)).grid(row=17, column=1, pady="10")
reader_name_label = Label(root, text="Name").grid(row=18, column=0, columnspan=2, sticky=W, padx=10)
reader_id_label = Label(root, text="ID").grid(row=19, column=0, columnspan=2, sticky=W, padx=10)
reader_address_label = Label(root, text="Address").grid(row=20, column=0, columnspan=2, sticky=W, padx=10)
reader_phone_label = Label(root, text="Phone #").grid(row=21, column=0, columnspan=2, sticky=W, padx=10)

#Entry boxes
reader_name_box = Entry(root).grid(row=18, column=1, pady=5)
reader_id_box = Entry(root).grid(row=19, column=1, pady=5)
reader_address_box = Entry(root).grid(row=20, column=1, pady=5)
reader_phone_box = Entry(root).grid(row=21, column=1, pady=5)

#Button
book_add_button = Button(root, text="ADD").grid(row=22, column=1, padx=10, pady=10)


root.mainloop()
