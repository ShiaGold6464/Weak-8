from distutils.command.config import config
from unittest import result
from zoneinfo import available_timezones
import mysql.connector 
from mysql.connector import errorcode

def get_available_books (config):
    db = mysql.connector.connect(**config)
    cursor1 = db.cursor()
    cursor1.execute("call get_available_books()") 
    books = cursor1.fetchall()
    return books 

def get_store_locations (config):
    db = mysql.connector.connect(**config)
    cursor2 = db.cursor()
    cursor2.execute("call get_store_locations()") 
    locations = cursor2.fetchall()
    return locations

def user_is_valid (current_user_id, config):
    db = mysql.connector.connect(**config)
    cursor3 = db.cursor()
    sql = "call validate_user_id({})".format(current_user_id) 
    print (sql)
    cursor3.execute("call validate_user_id({})".format(current_user_id)) 
    results = cursor3.fetchall()
    for  result in results: 
        if result[0] == 1:
            return True
        else :
            return False  

def get_user_wishlist_books (current_user_id, config):
    db = mysql.connector.connect(**config)
    cursor4 = db.cursor()
    sql4 = "call get_user_wishlist_books({})".format(current_user_id)
    print (sql4)
    cursor4.execute(sql4)
    wishlist_books = cursor4.fetchall()
    return wishlist_books

def add_user_wishlist_book (current_user_id, new_book_id, config):
    db = mysql.connector.connect(**config)
    cursor5 = db.cursor()
    #sql5 = "insert into wishlist (user_id, book_id) values ({}, {})".format(current_user_id, new_book_id)
    sql5 = "call add_user_wishlist_book({}, {})".format(current_user_id, new_book_id)
    print (sql5)
    cursor5.execute(sql5) 
    db.commit ()
    return True 









def main():

    config = {
        "user": "whatabook_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "whatabook",
        "raise_on_warnings": True
    }
    try:
        db = mysql.connector.connect(**config)
        print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))\
    
        print("")

        print("Whatabook Main Menu")
        print("")

        print("   1. View Books")
        print("   2. View Store Locations")
        print("   3. My Account")
        print("   4. Exit Program")

        while True: 
            try: 
                print("")
                main_menu_choice = input("Please choose a main menu option: ")
               
                if main_menu_choice == "1": 
                    books = get_available_books (config)
                    for book in books: 
                        print("Book name: {}".format(book[1]))

                elif main_menu_choice == "2": 
                    locations =get_store_locations(config)
                    for location in locations: 
                        print("location : {}".format(location[1]))

                elif main_menu_choice == "3":
                    user_id_input = input("Please eneter your user id: ")
                    if not user_is_valid(user_id_input, config):
                        print("User id not found !") 
                    else :
                        print("User Menu")
                        print("")

                        print("   1. Wishlist")
                        print("   2. Add Book ")
                        print("   3. Main Menu")

                        while True:

                            user_menu_choice = input("Please choose a user menu option: ")
                            if user_menu_choice == "1":
                                wishlist_books = get_user_wishlist_books(user_id_input, config)
                                for wishlist_book in wishlist_books: 
                                    print("wishlist book : {}".format(wishlist_book[1]))

                            elif user_menu_choice == "2":
                                print ("")
                                print ("Available books:")
                                available_books = get_available_books (config)
                                for available_book in available_books: 
                                    print("Book ID: {}, Book name: {}, Author: {}, Description: {}".format(available_book[0], available_book[1], available_book[2], available_book[3]))
                                new_book_id = input ("Please enter a book id")
                                add_user_wishlist_book (user_id_input, new_book_id, config)

                            elif user_menu_choice == "3":
                                break 

                elif main_menu_choice == "4":
                    break 

            except Exception as e:
                print("Oops!", e.__class__, "occurred.")

                continue
    
    #if main_menu_choice not in ["1","2","3"]:
        #print(" incorrect chose please try again ") 
    #else :
        #print ("ok")
    except mysql.connector.Error as err:
        if err.errno== errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print( "The specified database does not exist")
        else:
            print(err)
    finally:
        db.close()


main()

        
