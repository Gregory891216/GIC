from MyLibrary import *
import pytest

@pytest.mark.hello
def testCreateDatabase():
    ml = MyLibrary()
    expected = "myDB"
    value = ml.createDatabase()
    assert value == expected 

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

@pytest.mark.initTable
def testInitDataBorrowedBooks():
    ml = MyLibrary("myDB")
    table_name = 'borrowed_books'
    sql = f'''
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (0, 4628538, 10, '2022-04-09', '2022-04-28'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (1, 88270203, 10, '2022-04-25', '2022-12-11'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (6, 88270203, 58, '2022-05-28', '2022-06-25'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (8, 53572776, 10, '2022-07-28', '2022-08-05'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (9, 2023748, 10, '2022-02-19', '2022-03-14'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (19, 19173054, 10, '2022-01-04', '2022-01-13'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (97, 88270203, 90, '2022-07-19', '2022-08-17'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (310, 2990996, 97, '2022-09-19', '2022-10-02'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (500, 38347870, 90, '2022-06-02', '2022-07-05'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (805, 96925225, 4, '2022-05-22', '2022-06-09'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (6533, 4628538, 6, '2022-08-14', '2022-09-03'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (8547, 40576510, 13, '2022-07-01', '2022-06-27'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20877, 28691365, 90, '2022-12-04', '2022-12-21'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20878, 95118284, 13, '2022-10-15', '2022-10-16'),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20879, 4628538, 13, '2022-10-15', NULL),
        (`borrow_id`, `user_id`, `book_id`, `borrow_date`, `return_date`) VALUES (20880, 96925225, 13, '2022-10-15', NULL);
    '''
    value = ml.initData(table_name, sql)
    print(value)

    assert value == 16 

@pytest.mark.initTable
def testInitDataUsers():
    ml = MyLibrary("myDB")
    table_name = 'users'
    sql = f'''
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (1191769, 'Weston', 'Osinski', 'elyse00@example.com', '1999-03-17'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (2023748, 'Hudson', 'Daugherty', 'xromaguera@example.org', '1975-05-14'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (2990996, 'Bernhard', 'Corkery', 'schowalter.madalyn@example.net', '2019-04-28'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (4628538, 'Isaiah', 'Keeling', 'sonia87@example.net', '1987-10-07'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (4914839, 'Elenor', 'Erdman', 'bskiles@example.org', '1989-02-10'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (17608084, 'Freeda', 'Rosenbaum', 'abbott.francesco@example.org', '1974-11-20'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (19173054, 'Imelda', 'Moore', 'rath.roosevelt@example.net', '1982-07-01'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (21321221, 'Don', 'Willms', 'beier.jayme@example.net', '1976-05-21'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (23606005, 'Caitlyn', 'Ritchie', 'josiah54@example.com', '1978-09-07'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (28691365, 'Louisa', 'Crona', 'warren.gutkowski@example.org', '2006-08-02'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (38347870, 'Colby', 'Wisozk', 'garrick89@example.com', '2011-04-21'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (40576510, 'Nikki', 'Rosenbaum', 'kkeeling@example.org', '1971-03-19'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (43076253, 'Jerrod', 'Parker', 'ecronin@example.net', '1986-09-27'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (50522491, 'Keira', 'Wolff', 'giuseppe24@example.net', '1981-09-04'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (52207709, 'Ozella', 'Harris', 'zyundt@example.org', '2020-10-11'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (53572776, 'Rowena', 'Blanda', 'natasha11@example.org', '1976-03-28'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (88270203, 'Karley', 'Keefe', 'frances04@example.org', '2015-01-29'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (95118284, 'Zackery', 'Satterfield', 'ortiz.lance@example.com', '1974-08-01'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (96925225, 'David', 'Abernathy', 'bernier.devin@example.net', '1975-06-18'),
        (`user_id`, `first_name`, `last_name`, `email`, `registration_date`) VALUES (99324490, 'Therese', 'Schultz', 'rasheed93@example.org', '2022-08-22');
    '''
    value = ml.initData(table_name, sql)
    print(value)

    assert value == 20 