import mysql.connector

class MyLibrary:
    def __init__(self, db_name=None):
        self.__hello = "hello world"
        self.__config = {"user":"root", "password":"SO7vkkillgw", "host":"localhost", "database":db_name}
        self.__conn = mysql.connector.connect(**self.__config)

    def printStuff(self):
        return self.__hello

    def createDatabase(self):
        try:
            with self.__conn.cursor() as cursor:

                sql = "CREATE DATABASE IF NOT EXISTS myDB;"

                cursor.execute(sql)
                
                # Retrive the newly create db
                cursor.execute("SHOW DATABASES LIKE 'myDB'")
                database_list = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return database_list[0][0]

    def createTable(self, table_name, sql):
        try:
            with self.__conn.cursor() as cursor:          
                cursor.execute(sql)
                
                # Retrive the newly create table
                cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
                table_list = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return table_list[0][0]

    def initData(self, table_name,  sql_values):
        '''
        Init a table with an sql statement

        return:
        total rows
        '''
        sql = f'INSERT INTO `{table_name}` (`book_id`, `title`, `author`, `publication_year`, `isbn`) VALUES ' + sql_values
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table_name}")
                cursor.execute(sql)
                

                sql_total_row = f"SELECT COUNT(*) FROM {table_name}"
                cursor.execute(sql_total_row)

                total_rows = cursor.fetchone()[0]
                self.__conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
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
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                borrowed_book_list = cursor.fetchall()
            
            print("Top 10 most borrowed books:")
            for book in borrowed_book_list:
                print(f"Book ID: {book[0]}, Title: {book[1]}, Times Borrowed: {book[2]}")
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return borrowed_book_list

    def getUserWhoBorrowedTheMost(self):
        '''
        Return the details of the user who borrowed the most book
        TODO:
        Get the max times_borrowed
        Search for the users that borrowed the same amount as max times_borrowed
            Returns:

        '''
        # sql = '''
        #     SELECT u.user_id, u.first_name, u.last_name, u.email, u.registration_date, bb.times_borrowed
        #     FROM users u
        #     INNER JOIN 
        #     (SELECT user_id, count(user_id) AS times_borrowed FROM borrowed_books GROUP BY user_id) bb
        #     ON u.user_id = bb.user_id
        #     ORDER BY bb.times_borrowed DESC LIMIT 10;
        # '''
        sql='''
        WITH times_borrowed AS(
            SELECT u.user_id, u.first_name, u.last_name, u.email, u.registration_date, bb.times_borrowed,
                RANK() OVER (ORDER BY bb.times_borrowed DESC) ranking
            FROM users u
            INNER JOIN
            (SELECT user_id, count(user_id) AS times_borrowed FROM borrowed_books GROUP BY user_id) bb
            ON u.user_id = bb.user_id
        )
        SELECT * FROM times_borrowed WHERE ranking=1;
        '''
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                user_detail = cursor.fetchall()
            
            print("User who borrowed most books:")
            print(user_detail)
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return user_detail


    def createIndexOnBooksPublicationYear(self):
        '''
        Create index at publication year column of books
        '''
        sql = "CREATE INDEX publication_year_index ON books(publication_year);"
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                self.__conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        print("done")

    def getBooksAt2020IsNotBorrowed(self):
        '''
        Search for books that are published in 2020 and is not borrowed by any user
        
            Returns:
                result (list): A list of dictionary with book data containing book ID and title
        '''
        result = []
        sql = '''
            SELECT bb.borrow_date, u.first_name, u.last_name, bk.title, bb.user_id, bk.book_id, bk.publication_year
            FROM borrowed_books bb
            LEFT JOIN 
            (SELECT user_id, first_name, last_name FROM users) u
            ON u.user_id = bb.user_id
            RIGHT JOIN
            (SELECT book_id, title, publication_year FROM books WHERE publication_year=2020) bk
            ON bk.book_id = bb.book_id 
            WHERE bb.borrow_date IS NULL;
        '''
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                book_details = cursor.fetchall()
            
            for book in book_details:
                result.append({"book_id": book[5], "title":book[3]})
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return result

    def getUsersWhoBorrowedBooksByAuthor(self, author_name):
        '''
        Search for users that borrowed the book by author name
            Parameters:
                author_name (str): The name of author to search
            Returns:
                result (list): A list of user data containing user ID, first name and last name
        '''
        result = []

        sql = f'''
            SELECT bb.borrow_date, u.first_name, u.last_name, bk.title, bb.user_id, bk.book_id
            FROM borrowed_books bb
            LEFT JOIN 
            (SELECT user_id, first_name, last_name FROM users) u
            ON u.user_id = bb.user_id
            RIGHT JOIN
            (SELECT book_id, title, author FROM books WHERE author='{author_name}') bk
            ON bk.book_id = bb.book_id;

        '''
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                borrowed_books_details = cursor.fetchall()
            
            for book in borrowed_books_details:
                result.append({"user_id": book[4], "first_name": book[1], "last_name": book[2], "title":book[3], "borrow_date":book[0]})
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
        return result
    
    def createProcedureToCalculateAVGBorrowedDate(self):
        '''
        Create a stored procedure to calculate average number of days a book is borrowed before being returned.
            Parameters:
                None
            
            Returns:
                result (Boolean): True at successfully created the stored procedure, vice versa
        '''

        sql = '''
        CREATE PROCEDURE calculate_average_borrowing_days(IN returned_book_id INT, OUT average_days FLOAT)
        BEGIN
            SELECT AVG(DATEDIFF(return_date, borrow_date)) INTO average_days
            FROM borrowed_books
            WHERE book_id = returned_book_id AND return_date IS NOT NULL;
        END
        '''
        result = False
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                self.__conn.commit()
            
            result = True
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
            
        return result

    def calculateAverageBorrowedDays(self, book_id):
        '''
        Call a stored procedure to calculate average number of days a book is borrowed before being returned.
            Parameters:
                book_id (number): Book ID as input to calulcate average borrowing days
            
            Returns:
                result (number): average borrowing days
        '''
        result = 0
        try:
            with self.__conn.cursor() as cursor:
                args = [book_id, 0]
                result = cursor.callproc('calculate_average_borrowing_days', args)

            print(f"The average number of days the book ({book_id}) is borrowed before being returned is: {result[1]}")
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()
            
        return result[1]
    
    def createTriggerToUpdateReturnDate(self):
        '''
        Create a trigger to that automatically updates the return_date in the borrowed_books table 
        to the current date when a book is returned.
            
            Parameters:
                None
            
            Returns:
                result (Boolean): True at successfully created the trigger, vice versa
        '''
        result = False
        sql = '''
        CREATE TRIGGER update_book_return_date
        BEFORE UPDATE ON borrowed_books
        FOR EACH ROW
        BEGIN
            IF OLD.return_date IS NULL THEN
                SET NEW.return_date = CURDATE();
            END IF;
        END
        '''
        
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
                self.__conn.commit()
            
            result = True
        except Exception as e:
            print(e)
        finally:
            self.closeConnection()

        return result
    
    def closeConnection(self):
        self.__conn.close()
    
    @property
    def getDBConnection(self):
        return self.__conn
        
    