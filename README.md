Generically Implemented Code (GIC)

Prerequisite python libraries:
    install coverage
    install pytest

Create the database by running test cases marked with table and initTable:
    coverage run -m pytest -vv test/testMyLibrary.py -s -m table
    coverage run -m pytest -vv test/testMyLibrary.py -s -m initTable

To run pytest with code coverage with the following example:
    coverage run -m pytest -vv test/testQueries.py -s -m getTop10MostBorrowedBook

    To prduce report:
    coverage html

To run test cases with code coverage:
    coverage run -m pytest -vv test/testQueries.py
    coverage html

    results are stored in:
    htmlcov/index.html


