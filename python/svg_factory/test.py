import unittest

from examples.svg_factory.svg_factory import SVGFactory


class Test(unittest.TestCase):
    templates_dir = 'ng_django/examples/svg_factory/templates'
    build_dir = 'ng_django/examples/svg_factory/build'
    html_filename = 'index.html'
    png_filename = 'index.png'

    def test(self):
        expected = """<circle cx='100' cy='100' r='100' fill='#adadaf'>"""
        factory = SVGFactory(self.templates_dir, self.build_dir)
        circle = factory.make_circle(cx=100, cy=100, r=100, fill='#adadaf')
        factory.add(circle)

        result = factory.build()

        self.assertIn(expected, result)
        factory.save_html(self.html_filename)
        factory.save_png(self.png_filename)
