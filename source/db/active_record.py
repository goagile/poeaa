"""


[title]: # (Активная запись)


Активная запись
===============

Импортируем модуль по работе с базой sqlite3

    >>> import sqlite3

Создаем соединение с базой и таблицу Persons

    >>> conn = sqlite3.connect(':memory:')
    >>> c = conn.cursor()
    >>> c = c.execute("CREATE TABLE Persons (PersonId text, LastName text, Age text)")
    >>> conn.commit()

Активная запись Person
----------------------

    >>> class Person:
    ...     connection = None
    ...     cursor = None
    ...     _insert_statement = "INSERT INTO Persons VALUES ('{}', '{}', '{}')"
    ...     _select_all_statement = "SELECT * FROM Persons"
    ...     _ids = iter(range(5))
    ... 
    ...     def __init__(self, last_name, age, id=None):
    ...         self.last_name = last_name
    ...         self.age = age
    ...         self.id = id
    ... 
    ...     def insert(self):
    ...         new_id = self.new_id()
    ...         self.cursor = self.cursor.execute(
    ...             self._insert_statement.format(new_id, self.last_name, self.age))
    ...         self.connection.commit()
    ...     
    ...     @classmethod
    ...     def find_all_persons(cls):
    ...         c = cls.cursor.execute("SELECT * FROM Persons")    
    ...         result = [cls.cast(row) for row in c.fetchall()] 
    ...         return result
    ...     
    ...     @classmethod
    ...     def find_by_last_name(cls, last_name):
    ...         find_statement = "SELECT * FROM Persons WHERE LastName='{}'"
    ...         c = cls.cursor.execute(find_statement.format(last_name))
    ...         result = cls.cast(c.fetchone())
    ...         return result 
    ... 
    ...     @classmethod
    ...     def cast(cls, row):
    ...         return Person(id=int(row[0]), last_name=row[1], age=int(row[2]))
    ...
    ...     @classmethod
    ...     def new_id(cls):
    ...         return next(cls._ids)

Настраиваем объект Person на работу с базой данных

    >>> Person.connection = conn
    >>> Person.cursor = c

Используем акивную запись Persons

    >>> sidorov = Person('Сидоров', 32)
    >>> sidorov.insert()

Добавим еще одну запись, можно кратко

    >>> Person('Петров', 25).insert()

Проверим, что в базу добавились новые записи 

    >>> c = c.execute("SELECT * FROM Persons")
    >>> c.fetchall()
    [('0', 'Сидоров', '32'), ('1', 'Петров', '25')]

Найдем клиента по фамилии

    >>> petrov = Person.find_by_last_name('Петров')
    >>> (petrov.last_name, petrov.age)
    ('Петров', 25)
    
Итерируем по найденым объектам

    >>> for person in Person.find_all_persons():
    ...     (person.last_name, person.age)
    ('Сидоров', 32)
    ('Петров', 25)

Особености паттерна
-------------------

- есть объект модели предметной области Person
- объект сам себя сохраняет в базе данных
- база данных скрыта в объекте предметной области
- методы поиска в базе данных реализованы через статические методы класса Person


"""
