from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("325x450")

# MySQL Connection
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
# print(my_db)

my_cursor = my_db.cursor()


# TABLES
# library Branch
my_cursor.execute("CREATE TABLE IF NOT EXISTS library_branch(lib_id INTEGER(10) PRIMARY KEY, "
                  "branch_name VARCHAR(155), branch_location VARCHAR(255))")

# Author
my_cursor.execute("CREATE TABLE IF NOT EXISTS author(author_id INTEGER(10) PRIMARY KEY, author_name VARCHAR(155))")

# Publisher
my_cursor.execute("CREATE TABLE IF NOT EXISTS publisher(publisher_id INTEGER(10) PRIMARY KEY, "
                  "publisher_address VARCHAR(255))")

# DATA INPUT
# Branch
branch_input = "INSERT INTO library_branch(lib_id, branch_name, branch_location)" \
               "VALUES(%s, %s, %s)"
library_branch = [
    (1234, "Sterling", "Manhattan"),
    (84, "Lloyd", "Queens"),
    (147, "General Ford", "Brooklyn"),
    (269, "Robert Hill", "Long Island")
    (74, "Library of Modern Arts", "Staten Island")
    (1, "New York Institute of Technology Library", "Manhatten")
]

my_cursor.executemany(branch_input, library_branch)

my_db.commit()

# Author
author_input = "INSERT INTO author(author_id, author_name)" \
               "VALUES(%s, %s)"
author_info = [
    (1231, "Malcolm X"),
    (186, "Owens Q"),
    (786, "Duke U"),
    (179, "Grisham A"),
    (2985, "Jewell B"),
    (7891, "Chouinard C"),
    (1749, "Westover A"),
    (4798, "Michaelides P"),
    (156, "Hunter J"),
    (79856, "Ng W"),
    (1354, "Greyson V"),
    (4798, "McMorris T"),
    (17984, "Driscoll H"),
    (47985, "Fisher P"),
    (17985, "Tigner E"),
]

my_cursor.executemany(author_input, author_info)

my_db.commit()


# Publisher
publisher_input = "INSERT INTO publisher(publisher_id, publisher_address)" \
               "VALUES(%s, %s)"
publisher_info = [
    (1231, "5 Mulberry Ave., London, UK"),
    (1219, "12 Murry Hill Road, Queens, New York, U.S., 11375"),
    (789, "W 61 Street, Manhatten, New York, U.S., 11323")
    (1415, "E 117 Street, Cleveland, Ohio, U.S. 44106),
    (945, "6 Pine Brook Blvd, Hartsdale, New York, 13723),
     (14758, "8 Main Street, Hightstown, New Jersey, 08520")
]

my_cursor.executemany(publisher_input, publisher_info)

my_db.commit()


# TKINTER
title_label = Label(root, text="Main Menu", font=("Helvetica", 20))
title_label.grid(row=1, column=0, columnspan=2, pady="12")

title_label = Label(root, text="Reader Login", font=("Helvetica", 17))
title_label.grid(row=2, column=0, columnspan=2, pady="12")


# READER Login Form
card_number_label = Label(root,text="Card No.").grid(row=3, column=0, sticky=W, padx=10)
reader_name_label = Label(root,text="Name").grid(row=4, column=0, sticky=W, padx=10)

# Entry Boxes
card_number_box = Entry(root)
card_number_box.grid(row=3, column=1, pady=5)

reader_name_box = Entry(root)
reader_name_box.grid(row=4, column=1)

# ADMIN Login Form
title_label = Label(root, text="\nAdministrative Login", font=("Helvetica", 17))
title_label.grid(row=7, column=0, columnspan=2, pady="12")

admin_id_label = Label(root,text="Admin ID").grid(row=8, column=0, sticky=W, padx=10)
admin_name_label = Label(root,text="Name").grid(row=9, column=0, sticky=W, padx=10)

# Entry Boxes
admin_id_box = Entry(root)
admin_id_box.grid(row=8, column=1, pady=5)

admin_name_box = Entry(root)
admin_name_box.grid(row=9, column=1, pady=10)

# Login Buttons
reader_login_button = Button(root, text="Login")
reader_login_button.grid(row=5, column=1, padx=5, pady=10)

admin_login_button = Button(root, text="Login")
admin_login_button.grid(row=10, column=1, padx=5, pady=10)


my_cursor.execute("SELECT * FROM library_branch")
result = my_cursor.fetchall()
for x in result:
    print(x)

my_cursor.execute("SELECT * FROM author")
result = my_cursor.fetchall()
for x in result:
    print(x)

my_cursor.execute("SELECT * FROM publisher")
result = my_cursor.fetchall()
for x in result:
    print(x)

root.mainloop()
