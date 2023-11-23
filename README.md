install coverage
install pytest


To run pytest with code coverage:
coverage run -m pytest -vv test/testMyLibrary.py -s -m getBooksAt2020IsNotBorrowed

To prduce report:
coverage html
