import unittest


class Test(unittest.TestCase):

    def test(self):
        expected = "<svg><circle cx='100' cy='100' r='50' fill='black'></circle></svg>"
        proxy = SVGProxy(SVGBuilder)
        proxy.circle(cx=100, cy=100, r=50)

        result = proxy.save()

        self.assertEqual(expected, result)


class SVGProxy:
    """ Класс-заместитель для построителя SVG """
    def __init__(self, svg_class):
        self.svg_class = svg_class
        self.commands = []

    def circle(self, cx, cy, r, fill='black'):
        """ Метод реализует отложенный вызов функций SVGBuilder """
        self.commands.append((self.svg_class.circle, cx, cy, r, fill))

    def save(self):
        """ Метод создает экземпляер класса SVGBuilder и вызавыет все его функции """
        instance = self.svg_class()
        for function, *args  in self.commands:
            function(instance, *args)
        return instance.save()


class SVGBuilder:

    def __init__(self):
        self.svg = '<svg>{items}</svg>'
        self.items = []

    def circle(self, cx, cy, r, fill='black'):
        template = "<circle cx='{}' cy='{}' r='{}' fill='{}'></circle>"
        self.items.append(template.format(cx, cy, r, fill))

    def save(self):
        return self.svg.format(items='\n'.join(self.items))
