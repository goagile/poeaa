"""


[title]: # (Маппер)


Маппер
======

Импортируем модуль по работе с базой sqlite3

    >>> import sqlite3

Создаем соединение с базой и таблицу Persons

    >>> conn = sqlite3.connect(':memory:')
    >>> c = conn.cursor()
    >>> c = c.execute("CREATE TABLE Persons (PersonId text, LastName text, Age text)")
    >>> conn.commit()

Объект предметной области Person
--------------------------------

    >>> class Person:
    ... 
    ...     def __init__(self, last_name, age, id=None):
    ...         self.last_name = last_name
    ...         self.age = age
    ...         self.id = id

Маппер
------

    >>> class PersonDataMapper:
    ...     _insert_statement = "INSERT INTO Persons VALUES ('{}', '{}', '{}')"
    ...     _select_all_statement = "SELECT * FROM Persons"
    ...     _ids = iter(range(5))
    ...
    ...     def __init__(self, connection):
    ...         self.connection = connection
    ...         self.cursor = connection.cursor()
    ...         
    ...     def insert(self, person: Person):
    ...         new_id = self.new_id()
    ...         self.cursor = self.cursor.execute(
    ...             self._insert_statement.format(new_id, person.last_name, person.age))
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
    ...         result = self.cast(c.fetchone())
    ...         return result
    ...
    ...     def cast(self, row):
    ...         return Person(id=int(row[0]), last_name=row[1], age=int(row[2]))
    ...
    ...     def new_id(self):
    ...         return next(self._ids)


Создаем новый маппер для Клиента

    >>> mapper = PersonDataMapper(conn)

Создаем объект предметной области Person и сохраняем его в базе с помощью маппера

    >>> sidorov = Person('Сидоров', 32)
    >>> mapper.insert(sidorov)

Добавим еще одну запись

    >>> petrov = Person('Петров', 25)
    >>> mapper.insert(petrov)

Проверим, что в базу добавились новые записи 

    >>> c = c.execute("SELECT * FROM Persons")
    >>> c.fetchall()
    [('0', 'Сидоров', '32'), ('1', 'Петров', '25')]

Найдем клиента по фамилии

    >>> petrov = mapper.find_by_last_name('Петров')
    >>> (petrov.last_name, petrov.age)
    ('Петров', 25)
    
Итерируем по найденым объектам

    >>> for person in mapper.find_all_persons():
    ...     (person.last_name, person.age)
    ('Сидоров', 32)
    ('Петров', 25)

Особености паттерна
-------------------

- все обязанности по работе с базой собраны в маппере
- объект предметной области не знает о маппере
- база данных не знает об объекте предметной области
- маппер знает об объекте предметной облати и о базе данных
- маппер можно будет поменять, это не затронет базу и объект предметной области
- базу можно будет поменять, это не затронет предметную область


"""
