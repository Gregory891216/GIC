import mysql.connector

class MyLibrary:
    def __init__(self, db_name=None):
        self.__hello = "hello world"
        self.__config = {"user":"root", "password":"SO7vkkillgw", "host":"localhost", "database":db_name}
        self.__conn = mysql.connector.connect(**self.__config)

    def printStuff(self):
        return self.__hello

    def createDatabase(self):
        with self.__conn.cursor() as cursor:

            sql = "CREATE DATABASE IF NOT EXISTS myDB;"

            cursor.execute(sql)
            
            # Retrive the newly create db
            cursor.execute("SHOW DATABASES LIKE 'myDB'")
            database_list = cursor.fetchall()

        return database_list[0][0]

    def createTable(self, table_name, sql):
        with self.__conn.cursor() as cursor:          
            cursor.execute(sql)
            
            # Retrive the newly create table
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            table_list = cursor.fetchall()

        return table_list[0][0]

    def initData(self, table_name,  sql_values):
        '''
        Init a table with an sql statement

        return:
        total rows
        '''
        sql = f'INSERT INTO `{table_name}` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES ' + sql_values
        with self.__conn.cursor() as cursor:
            cursor.execute(f"DELETE FROM {table_name}")
            cursor.execute(sql)
            

            sql_total_row = f"SELECT COUNT(*) FROM {table_name}"
            cursor.execute(sql_total_row)

            total_rows = cursor.fetchone()[0]
            self.__conn.commit()

        return total_rows

    def getTop10MostBorrowedBook(self):
        '''
        Get top ten of most borrowed book

        return:
        list
        '''
        result = []
        #sql = 'SELECT book_id, count(book_id) AS times_borrowed FROM borrowed_books GROUP BY book_id LIMIT 10; '

        sql = '''
            SELECT bk.book_id, bk.title AS book_title, bb.times_borrowed
            FROM books bk
            INNER JOIN 
            (SELECT book_id, count(book_id) AS times_borrowed FROM borrowed_books GROUP BY book_id) bb
            ON bb.book_id = bk.book_id
            ORDER BY times_borrowed DESC LIMIT 10;
        '''
        
        with self.__conn.cursor() as cursor:
            cursor.execute(sql)
            borrowed_book_list = cursor.fetchall()
        
        print("Top 10 most borrowed books:")
        for book in borrowed_book_list:
            print(f"Book ID: {book[0]}, Title: {book[1]}, Times Borrowed: {book[2]}")

        return borrowed_book_list

    def getUserWhoBorrowedTheMost(self):
        '''
        Return the details of the user who borrowed the most book
        
        return:

        '''
        sql = '''
            SELECT u.user_id, u.first_name, u.last_name, u.email, u.registration_date, bb.times_borrowed
            FROM users u
            INNER JOIN 
            (SELECT user_id, count(user_id) AS times_borrowed FROM borrowed_books GROUP BY user_id) bb
            ON u.user_id = bb.user_id
            ORDER BY bb.times_borrowed DESC LIMIT 10;
        '''
        with self.__conn.cursor() as cursor:
            cursor.execute(sql)
            user_detail = cursor.fetchall()[0]
        
        print("User who borrowed most books:")
        print(user_detail)

        return user_detail


    def createIndexOnBooksPublicationYear(self):
        '''
        Create index at publication year column of books
        '''
        sql = "CREATE INDEX publication_year_index ON books(publication_year);"
        with self.__conn.cursor() as cursor:
            cursor.execute(sql)
            self.__conn.commit()
        print("done")

    def getBooksAt2020IsNotBorrowed(self):
        '''
        Search for books that are published in 2020 and is not borrowed by any user
        
        96 is not borrowed

        return:
        book_id
        '''
        sql = '''
            SELECT bb.borrow_date, u.first_name, u.last_name, bk.title, bb.user_id, bk.book_id, bk.publication_year
            FROM borrowed_books bb
            LEFT JOIN 
            (SELECT user_id, first_name, last_name FROM users) u
            ON u.user_id = bb.user_id
            RIGHT JOIN
            (SELECT book_id, title, publication_year FROM books WHERE publication_year=2020) bk
            ON bk.book_id = bb.book_id 
            WHERE bb.borrow_date IS NULL LIMIT 10;
        '''
        with self.__conn.cursor() as cursor:
            cursor.execute(sql)
            book_detail = cursor.fetchall()[0]
        return book_detail

    
    def closeConnection(self):
        self.__conn.close()
    
    def getDBConnection(self):
        return self.__conn
        
    