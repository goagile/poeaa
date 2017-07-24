import unittest

from design_patterns.factory import SVGFactory


class Test(unittest.TestCase):
    templates_dir = 'examples/python/svg_factory/templates'
    build_dir = 'examples/python/svg_factory/build'
    html_filename = 'index.html'
    png_filename = 'index.png'

    def test(self):
        expected = """<circle cx='200' cy='100' r='100' fill='#adadaf'>"""
        factory = SVGFactory(self.templates_dir, self.build_dir)
        circle = factory.make_circle(cx=200, cy=100, r=100, fill='#adadaf')
        factory.add(circle)

        result = factory.build()

        self.assertIn(expected, result)
