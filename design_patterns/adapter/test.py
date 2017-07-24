import unittest


class Test(unittest.TestCase):

    def test(self):
        expected = (
"""
my head
"""
        )

        writer = TextWriter()
        writer.header('my head')
        # writer.paragraph()
        # writer.footer()

        result = writer.content

        self.assertEqual(expected, result)


class TextWriter:

    def __init__(self):
        self.lines = []

    def header(self, text):
        self.lines.append(text)

    def content(self):
        return '\n'.join(self.lines)
