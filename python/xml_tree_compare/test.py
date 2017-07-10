import unittest
from python.xml_tree_compare.dom import XmlTree


class Test(unittest.TestCase):
    def test(self):
        xml1 = """
        <note>
            <to>Tove</to>
            <from>Jani</from>
            <heading>Reminder</heading>
            <body>Don't forget me this weekend!</body>
        </note>
        """

        xml2 = """
        <note>
            <to>Tove</to>
            <from>Jani</from>
            <heading>Remi3nder</heading>
            <body>Don't forget me this weekend!</body>
        </note>
        """

        self.assertXmlEqual(xml1, xml2)

    def assertXmlEqual(self, xml1, xml2):
        tree1 = XmlTree.convert_string_to_tree(xml1)
        tree2 = XmlTree.convert_string_to_tree(xml2)

        comparator = XmlTree()

        self.assertTrue(comparator.xml_compare(tree1, tree2, ["from"]))
