"""


[title]: # (Шлюз к таблице данных)


Шлюз к таблице данных
=====================

Импортируем модуль по работе с базой sqlite3
 
    >>> import sqlite3

Создаем соединение с базой и таблицу Persons

    >>> conn = sqlite3.connect(':memory:')
    >>> c = conn.cursor()
    >>> c = c.execute("CREATE TABLE Persons (PersonId text, LastName text, Age text)")
    >>> conn.commit()

Шлюз к таблице Persons
----------------------
Напишем шлюз к таблице Persons

    >>> class PersonTableGateway:
    ...     _insert_statement = "INSERT INTO Persons VALUES ('{}', '{}', '{}')"
    ...     _select_all_statement = "SELECT * FROM Persons"
    ...     _ids = iter(range(5))
    ... 
    ...     def __init__(self, connection):
    ...         self.connection = connection
    ...         self.cursor = connection.cursor()
    ... 
    ...     def insert_person(self, last_name, age):
    ...         c = self.cursor
    ...         new_id = self.new_id()
    ...         c = c.execute(self._insert_statement.format(new_id, last_name, age))
    ...         self.connection.commit()
    ...     
    ...     def find_all_persons(self):
    ...         c = self.cursor.execute("SELECT * FROM Persons")    
    ...         result = [self.cast(row) for row in c.fetchall()] 
    ...         return result
    ...     
    ...     def find_by_last_name(self, last_name):
    ...         find_statement = "SELECT * FROM Persons WHERE LastName='{}'"
    ...         c = self.cursor.execute(find_statement.format(last_name))
    ...         result = [self.cast(row) for row in c.fetchall()]
    ...         return result 
    ... 
    ...     def cast(self, row):
    ...         return int(row[0]), row[1], int(row[2])
    ...                  
    ...     def new_id(self):
    ...         return next(self._ids)

Используем шлюз к таблице Persons

    >>> table = PersonTableGateway(conn)
    >>> table.insert_person('Сидоров', 32)
    >>> table.insert_person('Петров', 25)
    >>> persons = table.find_all_persons()
    >>> persons
    [(0, 'Сидоров', 32), (1, 'Петров', 25)]
    
    >>> persons = table.find_by_last_name('Сидоров')
    >>> persons
    [(0, 'Сидоров', 32)]

Особености паттерна
-------------------

- нет модели предметной области (нет объекта Person)
- есть класс, представляющий всю таблицу Persons 
- при вставкеновой строки в таблицу поля не могут заполняться разрознено (отложено) и в любом порядке
- запись сразу вставляется в таблицу
- обязаности поиска и формирования сложного запроса определены в единственном классе таблицы
- таблица возвращает свои строки в виде списка кортэжей


"""
