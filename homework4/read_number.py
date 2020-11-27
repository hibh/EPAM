"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
Write a test for that function using pytest library.
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run
"""


def read_magic_number(path: str) -> bool:

    with open(path) as fi:
        first_line = fi.readline()
        if len(first_line) <= 0:
            raise ValueError("Empty file")
        first_line = int(first_line)
        if 1 <= first_line < 3:
            return True
        else:
            return False
