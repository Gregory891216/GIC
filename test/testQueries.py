from Queries import *
import pytest


@pytest.mark.getTop10MostBorrowedBook
def testGetTop10MostBorrowedBook():
    ml = Queries("myDB")
    value = ml.getTop10MostBorrowedBook()

    # Number 1 most read book id is 13
    assert value[0][0] == 13

@pytest.mark.getUserWhoBorrowedTheMost
def testGetUserWhoBorrowedTheMost():
    '''
    There are two person borrowed the most in the data
    user_id = 4628538 and user_id = 88270203
    '''
    ml = MyLibrary("myDB")
    value = ml.getUserWhoBorrowedTheMost()
    expected_uid = 88270203
    expected_first_name = "Karley"
    expected_last_name = "Keefe"
    assert len(value) == 2
    assert value[1][0] == expected_uid
    assert value[1][1] == expected_first_name
    assert value[1][2] == expected_last_name

@pytest.mark.createIndexOnBooksPublicationYear
def testCreateIndexOnBooksPublicationYear():
    ml = MyLibrary("myDB")
    value = ml.createIndexOnBooksPublicationYear()
    assert value == "Done"

@pytest.mark.getBooksAt2020IsNotBorrowed
def testGetBooksAt2020IsNotBorrowed():
    ml = MyLibrary("myDB")
    value = ml.getBooksAt2020IsNotBorrowed()

    expected_book_id = 96 # book id of 96 is not borrowed by any user and the publication year is 2020
    assert value[0]["book_id"] == expected_book_id


@pytest.mark.getUsersWhoBorrowedBooksByAuthor
def testGetUsersWhoBorrowedBooksByAuthor():
    author_name = "Mr. Benjamin Huel DVM"
    ml = MyLibrary("myDB")

    value = ml.getUsersWhoBorrowedBooksByAuthor(author_name)

    expected_return_size = 3
    expected_user_id_0 = 88270203
    expected_user_id_1 = 38347870
    expected_user_id_2 = 28691365
    
    assert value[0]["user_id"] == expected_user_id_0
    assert value[1]["user_id"] == expected_user_id_1
    assert value[2]["user_id"] == expected_user_id_2
    assert len(value) == expected_return_size


@pytest.mark.dependency(name="StoredProcedureAVGDays")
@pytest.mark.createStoredProcedure
def testCreateStoredProcedure():
    ml = MyLibrary("myDB")
    value = ml.createProcedureToCalculateAVGBorrowedDate()
    print (value)
    assert value == True
    
@pytest.mark.dependency(depends=["StoredProcedureAVGDays"])
@pytest.mark.callStoredProcedure
def testCalculateAverageBorrowedDays():
    # Using book_id = 4, average_days = 18.0
    ml = MyLibrary("myDB")
    expected_value = 18.0
    value = ml.calculateAverageBorrowedDays(4)
    assert value == expected_value
    

@pytest.mark.dependency(name="TriggerUpdateReturnDate")
@pytest.mark.createTrigger
def testCreateTriggerToUpdateReturnDate():
    ml = MyLibrary("myDB")
    value = ml.createTriggerToUpdateReturnDate()
    print(value)
    assert value == True

@pytest.mark.dependency(depends=["TriggerUpdateReturnDate"])
@pytest.mark.triggerUpdateReturnDate
def testTrigger():
    '''
    When a user returned a book, the borrowed_books table will be updated based on book_id and user_id
    and return date will be updated to current date

    For testing purposes, borrow_id=20879 will be used, simulating the book is being borrowed and
    using is going to return it.

    Once the book is returned, return_date will not be NULL

    '''
    ml = MyLibrary("myDB")
    
    sql = '''
        UPDATE borrowed_books 
        SET 
            book_id = 13
        WHERE
            user_id = 4628538;
        '''
    sql_result = '''
        SELECT * FROM borrowed_books WHERE borrow_id=20879;
    '''
    try:
        with ml.getDBConnection.cursor() as cursor:
            cursor.execute(sql)
            ml.getDBConnection.commit()

            cursor.execute(sql_result)
            borrowed_books_details = cursor.fetchone()
        
    except Exception as e:
        print(e)
    finally:
        ml.closeConnection()

        assert borrowed_books_details[4] is not None
    pass