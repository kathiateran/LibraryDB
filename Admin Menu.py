from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Library Database System')
root.geometry("770x720")

# MySQL Connection
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="LibraryDB"
)
# print(mydb)

my_cursor = my_db.cursor()

# TABLES
# Book data --> have to figure out how to have composite primary key, AUTO_INCREMENT PRIMARY KEY
my_cursor.execute("CREATE TABLE IF NOT EXISTS book_data(book_id INTEGER AUTO_INCREMENT, copy_no INTEGER, "
                  "book_branch VARCHAR(55), book_title VARCHAR(255), book_publisher VARCHAR(55),"
                  "book_author VARCHAR(155), publication_date DATE, "
                  "PRIMARY KEY(book_id, copy_no, book_branch))")

# Reader
my_cursor.execute("CREATE TABLE IF NOT EXISTS reader_data(reader_id INTEGER(10) PRIMARY KEY, "
                  "reader_name VARCHAR(155),"
                  "reader_address VARCHAR(255), reader_phone INTEGER(20))")


# book reader, Borrow date, return date
# my_cursor.execute("ALTER TABLE book_data ADD(book_reader VARCHAR(200), borrow_date DATE, return_date DATE)")

my_cursor.execute(
		"CREATE TABLE borrowRecord (" \
		"bdatetime DATE, rdatetime DATE," \
		"reader_record INTEGER(10), book_id_record INTEGER(10), copy_Record INTEGER(10)," \
		"branch_record INTEGER(10), PRIMARY KEY (bdatetime, book_id_record, copy_record, branch_record)," \
		"FOREIGN KEY (reader_record) REFERENCES reader_data(reader_id)," \
		"FOREIGN KEY (book_id_record) REFERENCES book_data(book_id)," \
		"FOREIGN KEY (copy_record) REFERENCES book_data(copy_no)," \
		"FOREIGN KEY (branch_Rrcord) REFERENCES book_data(book_branch),)"
)


def clear_fields():
    book_id_box.delete(0, END)
    copy_no_box.delete(0, END)
    book_title_box.delete(0, END)
    book_branch_box.delete(0, END)
    book_publisher_box.delete(0, END)
    book_author_box.delete(0, END)
    publication_date_box.delete(0, END)
    reader_name_box.delete(0, END)
    reader_id_box.delete(0, END)
    reader_address_box.delete(0, END)
    reader_phone_box.delete(0, END)


# Database Submissions
def add_book():
    sql_command = "INSERT INTO book_data (book_id, copy_no, book_branch, book_title, " \
                  "book_publisher, book_author, publication_date) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (book_id_box.get(), copy_no_box.get(), book_branch_box.get(), book_title_box.get(), book_publisher_box.get(), book_author_box.get(), publication_date_box.get())
    my_cursor.execute(sql_command, values)

    my_db.commit()
    clear_fields()

#Books
book_input = "INSERT INTO book_data (book_id, copy_no, book_branch, book_title, " \
                  "book_publisher, book_author, publication_date, book_reader) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
hardcoded_book_entities = [
    (1432589468,1,1,"AAAAA",1231,1231,11/12/1984,None),
(1432589468,2,1,"AAAAA",1231,1231,11/12/1984,None),
(1984756821,1,1,"Text 1",945,186,9/6/2001,None),
(1984756821,2,1,"Text 1",945,186,9/6/2001,None),
(1984756821,3,1,"Text 1",945,186,9/6/2001,None),
(2578931486,1,1,"Dictionary 2",789,786,12/11/2011,None),
(4294562872,1,1,"Booklet 4",945,2985,5/20/2002,None),
(4294562872,2,1,"Booklet 4",945,2985,5/20/2002,None),
(4948721547,1,1,"Book 5",1219,7891,8/16/2004,None),
(6045685147,1,1,"Magazine 6",945,1749,3/19/1998,None),
(6891205621,1,1,"Pamphlet 7",1231,4798,7/16/2008,None),
(7821158952,1,1,"Dictionary 8",945,156,10/10/2010,None),
(8965712354,1,1,"Textbook 10",14758,1354,1/30/2014,None),
(9089135478,1,1,"Textbook 11",1231,4798,1/1/2001,None),
(9174928472,1,1,"Textbook 12",1219,17984,8/14/2005,None),
(1432589468,1,74,"AAAAA",1231,1231,11/12/1984,None),
(1432589468,2,74,"AAAAA",1231,1231,11/12/1984,None),
(1432589468,3,74,"AAAAA",1231,1231,11/12/1984,None),
(1984756821,1,74,"Text 1",945,186,9/6/2001,None),
(2578931486,2,74,"Dictionary 2",789,786,12/11/2011,None),
(4294562872,1,74,"Booklet 4",945,2985,5/20/2002,None),
(4948721547,1,74,"Book 5",1219,7891,8/16/2004,None),
(4948721547,2,74,"Book 5",1219,7891,8/16/2004,None),
(6045685147,1,74,"Magazine 6",945,1749,3/19/1998,None),
(6891205621,1,74,"Pamphlet 7",1231,4798,7/16/2008,None),
(6891205621,2,74,"Pamphlet 7",1231,4798,7/16/2008,None),
(8965712354,1,74,"Textbook 10",14758,1354,1/30/2014,None),
(8965712354,2,74,"Textbook 10",14758,1354,1/30/2014,None),
(9174928472,1,74,"Textbook 12",1219,17984,8/14/2005,None),
(9174928472,2,74,"Textbook 12",1219,17984,8/14/2005,None),
(9374824156,1,74,"Study Guide 13",14758,47985,9/17/2003,None),
(1432589468,1,84,"AAAAA",1231,1231,11/12/1984,None),
(1984756821,1,84,"Text 1",945,186,9/6/2001,None),
(1984756821,2,84,"Text 1",945,186,9/6/2001,None),
(2578931486,1,84,"Dictionary 2",789,786,12/11/2011,None),
(2578931486,2,84,"Dictionary 2",789,786,12/11/2011,None),
(3789641258,1,84,"Pamphlet 3",1219,179,4/2/2003,None),
(4294562872,1,84,"Booklet 4",945,2985,5/20/2002,None),
(4294562872,2,84,"Booklet 4",945,2985,5/20/2002,None),
(4948721547,1,84,"Book 5",1219,7891,8/16/2004,None),
(6045685147,1,84,"Magazine 6",945,1749,3/19/1998,None),
(6045685147,2,84,"Magazine 6",945,1749,3/19/1998,None),
(6891205621,1,84,"Pamphlet 7",1231,4798,7/16/2008,None),
(7862351478,1,84,"Guidebook 9",1415,79856,1/11/1991,None),
(8965712354,1,84,"Textbook 10",14758,1354,1/30/2014,None),
(9174928472,1,84,"Textbook 12",1219,17984,8/14/2005,None),
(9374824156,1,84,"Study Guide 13",14758,47985,9/17/2003,None),
(9671586412,1,84,"Codex 14",789,17985,10/1/2015,None),
(1432589468,1,147,"AAAAA",1231,1231,11/12/1984,None),
(1432589468,2,147,"AAAAA",1231,1231,11/12/1984,None),
(2578931486,1,147,"Dictionary 2",789,786,12/11/2011,None),
(3789641258,1,147,"Pamphlet 3",1219,179,4/2/2003,None),
(3789641258,2,147,"Pamphlet 3",1219,179,4/2/2003,None),
(3789641258,3,147,"Pamphlet 3",1219,179,4/2/2003,None),
(4294562872,1,147,"Booklet 4",945,2985,5/20/2002,None),
(6045685147,1,147,"Magazine 6",945,1749,3/19/1998,None),
(6045685147,2,147,"Magazine 6",945,1749,3/19/1998,None),
(6045685147,3,147,"Magazine 6",945,1749,3/19/1998,None),
(7862351478,1,147,"Guidebook 9",1415,79856,12/20/2000,None),
(7862351478,2,147,"Guidebook 9",1415,79856,12/20/2000,None),
(7862351478,3,147,"Guidebook 9",1415,79856,12/20/2000,None),
(8965712354,1,147,"Textbook 10",14758,1354,1/30/2014,None),
(8965712354,2,147,"Textbook 10",14758,1354,1/30/2014,None),
(8965712354,3,147,"Textbook 10",14758,1354,1/30/2014,None),
(9089135478,1,147,"Textbook 11",1231,4798,1/1/2001,None),
(9174928472,1,147,"Textbook 12",1219,17984,8/14/2005,None),
(9374824156,1,147,"Study Guide 13",14758,47985,9/17/2003,None),
(1984756821,1,269,"Text 1",945,186,9/6/2001,None),
(3789641258,1,269,"Pamphlet 3",1219,179,4/2/2003,None),
(4294562872,1,269,"Booklet 4",945,2985,5/20/2002,None),
(4948721547,1,269,"Book 5",1219,7891,8/16/2004,None),
(4948721547,2,269,"Book 5",1219,7891,8/16/2004,None),
(4948721547,3,269,"Book 5",1219,7891,8/16/2004,None),
(6045685147,1,269,"Magazine 6",945,1749,3/19/1998,None),
(6891205621,1,269,"Pamphlet 7",1231,4798,7/16/2008,None),
(7862351478,1,269,"Guidebook 9",1415,79856,12/20/2000,None),
(8965712354,1,269,"Textbook 10",14758,1354,1/30/2014,None),
(9089135478,1,269,"Textbook 11",1231,4798,1/1/2001,None),
(9671586412,1,269,"Codex 14",789,17985,10/1/2015,None),
(9671586412,2,269,"Codex 14",789,17985,10/1/2015,None),
(1432589468,1,1234,"AAAAA",1231,1231,11/12/1984,None),
(1984756821,1,1234,"Text 1",945,186,9/6/2001,None),
(3789641258,1,1234,"Pamphlet 3",1219,179,4/2/2003,None),
(4948721547,1,1234,"Book 5",1219,7891,8/16/2004,None),
(6891205621,1,1234,"Pamphlet 7",1231,4798,7/16/2008,None),
(6891205621,2,1234,"Pamphlet 7",1231,4798,7/16/2008,None),
(8965712354,1,1234,"Textbook 10",14758,1354,1/30/2014,None),
(8965712354,2,1234,"Textbook 10",14758,1354,1/30/2014,None),
(9089135478,1,1234,"Textbook 11",1231,4798,1/1/2001,None),
(9089135478,2,1234,"Textbook 11",1231,4798,1/1/2001,None),
(9374824156,1,1234,"Study Guide 13",14758,47985,9/17/2003,None),
(9671586412,1,1234,"Codex 14",789,17985,10/1/2015,None)
]

my_cursor.executemany(book_input, hardcoded_book_entities)

my_db.commit()

def add_reader():
    sql_command = "INSERT INTO reader_data (reader_id, reader_name, reader_address, reader_phone)" \
                  "VALUES(%s, %s, %s, %s)"
    values = (reader_id_box.get(), reader_name_box.get(), reader_address_box.get(), reader_phone_box.get())
    my_cursor.execute(sql_command, values)

    my_db.commit()
    clear_fields()


# SEARCH functions
def search_records():
    book_search_list =Tk()
    book_search_list.title("Book Search Result")
    book_search_list.geometry("400x400")

    my_cursor.execute("SELECT * FROM book_data")
    s_result = my_cursor.fetchall()
    for x in s_result:
        lookup_label= Label(book_search_list, text=x)
        lookup_label.pack()
        # print(x)


# SEARCH function
def branch_info():
    branch_info_list =Tk()
    branch_info_list.title("Branch Information")
    branch_info_list.geometry("400x400")

    my_cursor.execute("SELECT * FROM library_branch")
    branch_result = my_cursor.fetchall()
    for x in branch_result:
        result_label= Label(branch_info_list, text=x)
        result_label.pack()


def top10_borrowers():
    top10_borrowers_list =Tk()
    top10_borrowers_list.title("Top 10 Borrowers in a Branch")
    top10_borrowers_list.geometry("400x400")
    
    sql_command = "SELECT reader_record COUNT(reader_record) FROM borrow_record" \
    "WHERE book_id_record, copy_record, branch_record IN" \
        "(SELECT book_id FROM book_data WHERE book_branch = (book_branch_id) VALUES(%s))" \
    "GROUP BY reader_record ORDER BY COUNT(Reader_Record) LIMIT 10"
    values = (book_branch_box.get())

    my_cursor.execute(sql_command, values)
    borrowers_result = my_cursor.fetchall()
    for x in borrowers_result:
        lookup_label= Label(top10_borrowers_list, text=x)
        lookup_label.pack()


def top10_books():
    top10_books_list = Tk()
    top10_books_list.title("Top 10 Most Borrowed Books in a Branch")
    top10_books_list.geometry("400x400")

    sql_command = "SELECT book_id_record COUNT(book_id_record) FROM borrow_record" \
	"WHERE book_id_record , copy_record, branch_record IN" \
		"(SELECT book_id, copy_no, book_branch FROM book_data" \
		"WHERE book_branch = (book_id)" \
        "VALUES(%s))"
	"GROUP BY book_id_record , copy_record, branch_record" \
	"ORDER BY COUNT(book_id_record , copy_record, branch_record) LIMIT 10"
    values = (book_branch_box.get())

    my_cursor.execute(sql_command, values)
    books_result = my_cursor.fetchall()
    for x in books_result:
        lookup_label = Label(top10_books_list, text=x)
        lookup_label.pack()


def average_fine():
    average_fine_list = Tk()
    average_fine_list.title("Average Fine Paid Per Reader")
    average_fine_list.geometry("400x400")
    
    sql_command =   "SELECT COUNT(Reader_Record) * 0.2 /" \
		                "(SELECT DISTINCT COUNT(reader_id)" \
		                "FROM reader_data)" \
                    "FROM BorrowRecord WHERE rdatetime - bdatetime >= 20"
    
    my_cursor.execute(sql_command)
    fine_result = my_cursor.fetchall()
    for x in fine_result:
        lookup_label = Label(average_fine_list, text=x)
        lookup_label.pack()


# TKINTER
am_title_label = Label(root, text="Administrative Menu", font=("Helvetica", 20)).grid(row=1, column=2, pady="12")

# BOOK SEARCH
sb_title_label = Label(root, text="Search Book", font=("Helvetica", 17)).grid(row=2, column=1, pady="12")
search_book_id_label = Label(root,text="ISBN").grid(row=3, column=0, sticky=E, padx=10)
search_book_title_label = Label(root,text="Title").grid(row=4, column=0, sticky=E, padx=10)
search_book_publisher_label = Label(root,text="Publisher").grid(row=5, column=0, sticky=E, padx=10)

# Entry Boxes
search_book_id_box = Entry(root)
search_book_id_box.grid(row=3, column=1, pady=5)
search_book_title_box = Entry(root)
search_book_title_box.grid(row=4, column=1, pady=5)
search_book_publisher_box = Entry(root)
search_book_publisher_box.grid(row=5, column=1, pady=5)

# Search Button
book_search_button = Button(root, text="Search", command=search_records)
book_search_button.grid(row=6, column=1, padx=5, pady=10)

# BOOK ADD
ab_title_label = Label(root, text="Add Book Copy", font=("Helvetica", 17)).grid(row=2, column=3, pady="12")
book_id_label = Label(root, text="ISBN").grid(row=3, column=2, sticky=E, padx=10)
copy_no_label = Label(root, text="Copy No.").grid(row=4, column=2, sticky=E, padx=10)
book_title_label = Label(root, text="Title").grid(row=5, column=2, sticky=E, padx=10)
book_branch_label = Label(root, text="Book Branch").grid(row=6, column=2, sticky=E, padx=10)
book_publisher_label = Label(root, text="Publisher").grid(row=7, column=2, sticky=E, padx=10)
book_author_label = Label(root, text="Author").grid(row=8, column=2, sticky=E, padx=10)
publication_date_label = Label(root, text="Publication Date").grid(row=9, column=2, sticky=E, padx=10)

# Entries
book_id_box = Entry(root)
book_id_box.grid(row=3, column=3, sticky=N, pady=10)
copy_no_box = Entry(root)
copy_no_box.grid(row=4, column=3, sticky=N, pady=10)
book_title_box = Entry(root)
book_title_box.grid(row=5, column=3, sticky=N, pady=10)
book_branch_box = Entry(root)
book_branch_box.grid(row=6, column=3, sticky=N, pady=10)
book_publisher_box = Entry(root)
book_publisher_box.grid(row=7, sticky=N, column=3, pady=10)
book_author_box = Entry(root)
book_author_box.grid(row=8, column=3, sticky=N, pady=10)
publication_date_box = Entry(root)
publication_date_box.grid(row=9, column=3, sticky=N, pady=10)

# Action Button
book_add_button = Button(root, text="Add Book", command=add_book).grid(row=10, column=3, padx=10, pady=10)

# READER ADD
ar_title_label = Label(root, text="Add New Reader", font=("Helvetica", 17)).grid(row=7, column=1, pady="15")
reader_name_label = Label(root, text="Name").grid(row=8, column=0, sticky=E, padx=10)
reader_id_label = Label(root, text="ID").grid(row=9, column=0, sticky=E, padx=10)
reader_address_label = Label(root, text="Address").grid(row=10, column=0, sticky=E, padx=10)
reader_phone_label = Label(root, text="Phone #").grid(row=11, column=0, sticky=E, padx=10)

# Entry boxes
reader_name_box = Entry(root)
reader_name_box.grid(row=8, column=1, pady=5)
reader_id_box = Entry(root)
reader_id_box.grid(row=9, column=1, pady=5)
reader_address_box = Entry(root)
reader_address_box.grid(row=10, column=1, pady=5)
reader_phone_box = Entry(root)
reader_phone_box.grid(row=11, column=1, pady=5)

# Button
reader_add_button = Button(root, text="Add Reader", command=add_reader).grid(row=12, column=1, padx=10, pady=10)

# Info buttons
top10_borrowers_label = Label(root, text="Top 10 borrowers in a branch.").grid(row=12, column=3, sticky=W, padx=10)
top10_borrowers_button = Button(root, text="Show", command= top10_borrowers).grid(row=12, column=2, sticky=E, padx=10, pady=10)

top10_books_label = Label(root, text="Top 10 most borrowed books in a branch.").grid(row=13, column=3, sticky=W, padx=10)
top10_books_button = Button(root, text="Show", command= top10_books).grid(row=13, column=2, sticky=E, padx=10, pady=10)

average_fine_label = Label(root, text="Average Fine Paid per Reader.").grid(row=14, column=3, sticky=W, padx=10)
average_fine_button = Button(root, text="Show", command= average_fine).grid(row=14, column=2, sticky=E, padx=10, pady=10)

branch_info_button = Button(root, text="BRANCH INFO", command=branch_info).grid(row=14, sticky=S, column=1, padx=10, pady=10)


my_cursor.execute("SELECT * FROM book_data")
result = my_cursor.fetchall()
for x in result:
    print(x)


my_cursor.execute("SELECT * FROM reader_data")
result = my_cursor.fetchall()
for x in result:
    print(x)


root.mainloop()
