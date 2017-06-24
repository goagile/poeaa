from unittest import TestCase, main


class TestPersonFinder(TestCase):
    """
        Пример реестра с явным интерфейсом доступа
    """

    def test_get_person_finder(self):
        expected_person = Person('Petrov', 'Ivan')
        fake_person_finder = FakePersonFinder({1: expected_person})
        Registry.set_person_finder(fake_person_finder)

        person_finder = Registry.get_person_finder()

        self.assertEqual(fake_person_finder, person_finder)

    def test_find_person(self):
        expected_person = Person('Petrov', 'Ivan')
        fake_person_finder = FakePersonFinder({1: expected_person})
        Registry.set_person_finder(fake_person_finder)
        person_finder = Registry.get_person_finder()

        person = person_finder.find_person(person_id=1)

        self.assertEqual(expected_person, person)


class Registry:
    def __init__(self):
        self.person_finder = None

    @classmethod
    def get_person_finder(cls):
        return cls.person_finder

    @classmethod
    def set_person_finder(cls, person_finder):
        cls.person_finder = person_finder


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        is_equal_params = all([
            self.last_name == other.last_name,
            self.first_name == other.first_name
        ])
        return is_equal_params


class FakePersonFinder:
    def __init__(self, dict_):
        self.dict_ = dict_

    def find_person(self, person_id):
        return self.dict_[person_id]


if __name__ == '__main__':
    main()
