Implementation of the following regular expression using state design pattern in python 3:

`(13)?\d\d[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])`

Usage Example:

`echo "Some text 1397-10-29 blah 1397-10-30 blah" | python3 main.py`

Output:

    1397-10-29
    1397-10-30
