from unittest import TestCase, main


class TestCalculator(TestCase):
    """
        Пример реестра с неявным интерфейсом доступа
    """

    def test_get_object(self):
        expected = FakeCalculator()
        Registry.put_object('calculator', expected)

        calculator = Registry.get_object('calculator')

        self.assertEqual(expected, calculator)

    def test_calc_sum(self):
        fake_calculator = FakeCalculator()
        Registry.put_object('calculator', fake_calculator)
        calculator = Registry.get_object('calculator')

        result = calculator.calc_sum([1, 3, 6, 5])

        self.assertEqual(15, result)


class FakeCalculator:
    def calc_sum(self, sequence):
        return sum(sequence)


class Registry:
    objects_ = dict()

    @classmethod
    def put_object(cls, name, object_):
        cls.objects_[name] = object_

    @classmethod
    def get_object(cls, name):
        return cls.objects_.get(name, None)


if __name__ == '__main__':
    main()
