import mysql.connector

class MyLibrary:
    def __init__(self, db_name=None):
        self.__config = {"user":"root", "password":"", "host":"localhost", "database":db_name}
        self.__conn = mysql.connector.connect(**self.__config)

    def createDatabase(self):
        '''
        Create a table with an sql statement
        Parameters:
            None
        Returns:
            database (str) : Schema of the table that has been created
        '''
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
        '''
        Create a table with an sql statement
        Parameters:
            table_name (str): name of the table to be created
            sql_values (str): sql string to create the table 
        Returns:
            table (str) : Schema of the table that has been created
        '''
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
        Parameters:
            table_name (str): name of the table initialize with data
            sql_values (str): data for the table 
        Returns:
            total_rows (number) : total rows added to the table
        '''
        total_rows = 0
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

    def closeConnection(self):
        self.__conn.close()
    
    @property
    def getDBConnection(self):
        return self.__conn
        
    