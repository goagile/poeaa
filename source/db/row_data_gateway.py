"""


[title]: # (Шлюз к записи данных)


Шлюз к записи данных
=====================

Импортируем модуль по работе с базой sqlite3

    >>> import sqlite3

Создаем соединение с базой и таблицу Persons

    >>> conn = sqlite3.connect(':memory:')
    >>> c = conn.cursor()
    >>> c = c.execute("CREATE TABLE Persons (PersonId text, LastName text, Age text)")
    >>> conn.commit()

Шлюз к записи Person
--------------------

    >>> class PersonRowGateway:
    ...     _insert_statement = "INSERT INTO Persons VALUES ('{}', '{}', '{}')"
    ...     _select_all_statement = "SELECT * FROM Persons"
    ...     _ids = iter(range(5))
    ... 
    ...     def __init__(self, connection):
    ...         self.connection = connection
    ...         self.cursor = connection.cursor()
    ...         self.last_name = None
    ...         self.age = None
    ... 
    ...     def insert(self):
    ...         new_id = self.new_id()
    ...         self.cursor = self.cursor.execute(
    ...             self._insert_statement.format(new_id, self.last_name, self.age))
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

    >>> sidorov_row = PersonRowGateway(conn)
    >>> sidorov_row.last_name = 'Сидоров'
    >>> sidorov_row.age = 32
    >>> sidorov_row.insert()
    
Проверим, что в базу добавилась новая запись 

    >>> c = c.execute("SELECT * FROM Persons")
    >>> c.fetchall()
    [('0', 'Сидоров', '32')]

Так как PersonRowGateway отражает одну строку таблицы
Для поиска потребуется другой класс, который будет искать строки таблицы

    >>> class PersonFinder:
    ...     find_by_id_statement = "SELECT * FROM Persons WHERE PersonId = '{}'"
    ...     def __init__(self, connection):
    ...         self.connection = connection
    ...         self.cursor = self.connection.cursor()
    ...     
    ...     def find_by_id(self, id):
    ...         self.cursor = self.cursor.execute(self.find_by_id_statement.format(id))
    ...         result = self.cast(self.cursor.fetchone())
    ...         return result
    ...
    ...     def cast(self, row):
    ...         person = PersonRowGateway(self.connection)
    ...         person.id = int(row[0])
    ...         person.last_name = row[1]
    ...         person.age = int(row[2])
    ...         return person

    >>> finder = PersonFinder(conn)
    >>> sidorov_row = finder.find_by_id(0)
    >>> (sidorov_row.id, sidorov_row.last_name, sidorov_row.age)
    (0, 'Сидоров', 32)

Добавим еще одного клиента
    
    >>> petrov = PersonRowGateway(conn)
    >>> petrov.last_name = 'Петров'
    >>> petrov.age = 45
    >>> petrov.insert()

Проверим, что в таблице теперь 2 клиента

    >>> c = c.execute("SELECT * FROM Persons")
    >>> c.fetchall()
    [('0', 'Сидоров', '32'), ('1', 'Петров', '45')]

Допишем метод для поиска всех клиентов

    >>> class PersonFinder:
    ...     find_by_id_statement = "SELECT * FROM Persons WHERE PersonId = '{}'"
    ...     find_all_statement = "SELECT * FROM Persons"
    ...
    ...     def __init__(self, connection):
    ...         self.connection = connection
    ...         self.cursor = self.connection.cursor()
    ...
    ...     def find_by_id(self, id):
    ...         self.cursor = self.cursor.execute(self.find_by_id_statement.format(id))
    ...         result = self.cast(self.cursor.fetchone())
    ...         return result
    ...
    ...     def cast(self, row):
    ...         person = PersonRowGateway(self.connection)
    ...         person.id = int(row[0])
    ...         person.last_name = row[1]
    ...         person.age = int(row[2])
    ...         return person
    ...     
    ...     def find_iter(self):
    ...         self.cursor = self.cursor.execute(self.find_all_statement)
    ...         return (self.cast(p) for p in self.cursor.fetchall())

Проитерируем по всем найденным записям

    >>> finder = PersonFinder(conn)
    >>> for person in finder.find_iter():
    ...     (person.id, person.last_name, person.age)
    (0, 'Сидоров', 32)
    (1, 'Петров', 45)

Особености паттерна
-------------------

- нет модели предметной области (нет объекта Person)
- есть класс, представляющий строку (одну запись) в таблице Persons 
- при вставкеновой строки в таблицу поля могут заполняться разрознено (отложено) и в любом порядке
- затем нужно подтвердить (закоммитить) свои действия методом insert
- обязаности поиска и формирования сложного запроса определены в отдельном классе PersonFinder


"""
