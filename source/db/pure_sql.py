"""


[title]: # (Чистый SQL)


    >>> import sqlite3

Запросы к базе данных напрямую
------------------------------
Используем запросы к базе данных

    >>> db1conn = sqlite3.connect(':memory:')
    >>> c = db1conn.cursor()
    
    >>> c = c.execute("CREATE TABLE Persons (LastName text, Age text)")

    >>> c = c.execute("INSERT INTO Persons VALUES ('{}', '{}')".format('Петров', 25))
    >>> db1conn.commit()

    >>> c = c.execute("SELECT * FROM Persons")    
    >>> c.fetchall()
    [('Петров', '25')]


"""
