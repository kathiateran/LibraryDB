from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("380x450")

# MySQL Connection
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
# print(mydb)

my_cursor = my_db.cursor()


# SEARCH functions
def search_book():
    book_search_list =Tk()
    book_search_list.title("Book Search Result")
    book_search_list.geometry("400x400")

    my_cursor.execute("SELECT * FROM book_data") # CHANGE!!
    s_result = my_cursor.fetchall()
    for x in s_result:
        lookup_label= Label(book_search_list, text=x)
        lookup_label.pack()
        # print(x)


# TKINTER
title_label = Label(root, text="Reader Menu", font=("Helvetica", 20))
title_label.grid(row=1, column=0, columnspan=2, pady="12")

# Book Search Form
title_label = Label(root, text="Search Book", font=("Helvetica", 17))
title_label.grid(row=2, column=0, columnspan=2, pady="12")

book_id_label = Label(root,text="Book ISBN").grid(row=3, column=0, sticky=W, padx=10)
book_title_label = Label(root,text="Title").grid(row=4, column=0, sticky=W, padx=10)
book_publisher_label = Label(root,text="Publisher").grid(row=5, column=0, sticky=W, padx=10)

# Entry Boxes
book_id_box = Entry(root)
book_id_box.grid(row=3, column=1, pady=5)

book_title_box = Entry(root)
book_title_box.grid(row=4, column=1, pady=5)

book_publisher_box = Entry(root)
book_publisher_box.grid(row=5, column=1, pady=5)

# Search Button
book_search_button = Button(root, text="Search", command=search_book)
book_search_button.grid(row=6, column=1, padx=5, pady=10)

# Book Actions
title_label = Label(root, text="Book Actions", font=("Helvetica", 17))
title_label.grid(row=10, column=0, columnspan=2, pady="12")

book_id_label = Label(root, text="Book ID", font=("Helvetica", 16))
book_id_label.grid(row=11, column=0, columnspan=2, sticky=W, padx=10)

book_publisher_box = Entry(root)
book_publisher_box.grid(row=11, column=1, pady=5)

# Action Buttons
book_reserve_button = Button(root, text="Reserve")
book_reserve_button.grid(row=12, column=0, padx=5, pady=10)

book_return_button = Button(root, text="Return")
book_return_button.grid(row=12, column=1, sticky=E, padx=5, pady=10)

book_checkout_button = Button(root, text="Checkout")
book_checkout_button.grid(row=12, column=1, sticky=W, pady=10)

root.mainloop()
