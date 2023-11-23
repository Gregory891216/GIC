from MyLibrary import *
import pytest

@pytest.mark.hello
def testHello():

    ml = MyLibrary()

    expected = "hello world"
    value = ml.printStuff()
    assert value == expected
    ml.closeConnection()


@pytest.mark.hello
def testCreateDatabase():
    ml = MyLibrary()
    expected = "myDB"
    value = ml.createDatabase()
    assert value == expected 
    ml.closeConnection()

@pytest.mark.table
def testCreateBooksTable():
    ml = MyLibrary("myDB")
    table_name = "books"
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                book_id INT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                publication_year INT,
                isbn VARCHAR(20)
            );'''

    value = ml.createTable(table_name, sql)
    assert value == table_name 
    ml.closeConnection()

@pytest.mark.table
def testCreateUsersTable():
    ml = MyLibrary("myDB")
    table_name = "users"
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                user_id INT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255),
                registration_date DATE
            );'''

    value = ml.createTable(table_name, sql)
    assert value == table_name 
    ml.closeConnection()

@pytest.mark.table
def testCreateBorrowedBooksTable():
    ml = MyLibrary("myDB")
    table_name = "borrowed_books"
    sql = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                borrow_id INT PRIMARY KEY,
                user_id INT,
                book_id INT,
                borrow_date DATE,
                return_date DATE,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)

            );'''

    value = ml.createTable(table_name, sql)
    assert value == table_name 
    ml.closeConnection()


@pytest.mark.initTable
def testInitData():
    ml = MyLibrary("myDB")
    table_name = 'books'
    sql = f'''
        (4, 'Nesciunt commodi ratione illum rerum.', 'Dr. Marques Jenkins DDS', 2018, 'smij'),
        (6, 'Maiores numquam laudantium qui soluta.', 'Vanessa Johnson', 2001, 'tsys'),
        (9, 'Sed consequatur qui est magnam sequi autem ducimus.', 'Rhianna Sipes', 2021, 'cskh'),
        (10, 'Amet laudantium repellat odit maxime molestiae nulla voluptas.', 'Drake Hagenes', 1998, 'pelb'),
        (13, 'Mollitia quia veritatis pariatur consequatur et.', 'Miss Luz Crooks', 1971, 'wcex'),
        (17, 'Est suscipit aperiam recusandae consequatur.', 'Mrs. Joanny Fahey', 2002, 'qnyy'),
        (25, 'Nesciunt ut odit cumque fugit.', 'Chris Keeling', 1987, 'nglp'),
        (29, 'Cumque dolorem distinctio ducimus iure non impedit ut.', 'Ladarius Moore', 1984, 'ctmw'),
        (48, 'Quia totam laboriosam sed ut nemo dolores laudantium.', 'Cody Hartmann DVM', 1992, 'umob'),
        (50, 'Aspernatur placeat quidem cum doloribus.', 'Lamar Feest', 2009, 'hvmq'),
        (56, 'Eveniet aliquam tenetur id laudantium at esse.', 'Ahmed Torphy', 1974, 'flgr'),
        (58, 'Quaerat quae nemo nisi.', 'Prof. Patsy Graham I', 2012, 'efjh'),
        (64, 'Sint alias consequatur accusantium repellat itaque.', 'Dr. Payton Treutel', 2017, 'vooa'),
        (69, 'Aperiam commodi voluptas eveniet soluta.', 'Mr. Mikel Kshlerin DDS', 2016, 'pntc'),
        (82, 'Facilis culpa excepturi soluta velit eligendi recusandae.', 'Micaela Pfeffer DDS', 1980, 'tfkf'),
        (84, 'Est provident ut iure ut velit.', 'Una Renner', 1970, 'lpnd'),
        (86, 'Deleniti voluptatem in numquam numquam.', 'Izaiah Hilll MD', 1980, 'ebhc'),
        (90, 'Eum architecto dignissimos et ut autem voluptas.', 'Mr. Benjamin Huel DVM', 2020, '0-1417-6042-7'),
        (96, 'Iste repellat qui dicta aliquid.', 'Dr. Dillan Lockman', 2020, '0-1384-3027-6'),
        (97, 'Aut ut iusto velit non rerum.', 'Mr. Kenneth Bashirian MD', 2020, '0-7642-8382-0');
    '''
    value = ml.initData(table_name, sql)
    print(value)

    assert value == 20 
    ml.closeConnection()


@pytest.mark.getTop10MostBorrowedBook
def testGetTop10MostBorrowedBook():
    ml = MyLibrary("myDB")
    value = ml.getTop10MostBorrowedBook()

    # Number 1 most read book id is 10
    assert value[0][0] == 10 
    ml.closeConnection()

@pytest.mark.getUserWhoBorrowedTheMost
def testGetUserWhoBorrowedTheMost():
    ml = MyLibrary("myDB")
    value = ml.getUserWhoBorrowedTheMost()
    expected_uid = 88270203
    expected_first_name = "Karley"
    expected_last_name = "Keefe"
    assert value[0] == expected_uid
    assert value[1] == expected_first_name
    assert value[2] == expected_last_name

@pytest.mark.createIndexOnBooksPublicationYear
def testCreateIndexOnBooksPublicationYear():
    with pytest.raises(Exception) as e:
        ml = MyLibrary("myDB")
        ml.createIndexOnBooksPublicationYear()
        print(e)

@pytest.mark.getBooksAt2020IsNotBorrowed
def testGetBooksAt2020IsNotBorrowed():
    ml = MyLibrary("myDB")
    value = ml.getBooksAt2020IsNotBorrowed()
    expected_book_id = 96
    assert value[5] == expected_book_id