import unittest
from os.path import join, dirname

from ocdev.plugins.appstore.infoparser import InfoParser
from ocdev.plugins.errors import DependencyError


class InfoParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = InfoParser()

    def load_file(self, name):
        folder = join(join(dirname(__file__), 'infos'))
        path = join(folder, name)
        with open(path, 'r') as f:
            text = f.read()
        return text

    def test_simple(self):
        xml = self.load_file('simple_info.xml')
        result = self.parser.parse(xml)
        self.assertEqual('My Test App', result['name'])
        self.assertEqual(925, result['category'])
        self.assertEqual('simple', result['description'])
        self.assertEqual('a', result['author'])
        self.assertEqual(16, result['licence'])
        self.assertEqual('0.0.1', result['version'])
        self.assertEqual('8', result['requiremin'])
        self.assertEqual('9', result['requiremax'])

    def test_simple_require(self):
        xml = self.load_file('simple_info_require.xml')
        result = self.parser.parse(xml)
        self.assertEqual('8', result['requiremin'])

    def test_simple_require_owncloud(self):
        xml = self.load_file('simple_info_require_owncloud.xml')
        result = self.parser.parse(xml)
        self.assertEqual('8', result['requiremin'])
        self.assertEqual('9', result['requiremax'])

    def test_simple_no_author(self):
        xml = self.load_file('simple_info_no_author.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_category(self):
        xml = self.load_file('simple_info_no_category.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_description(self):
        xml = self.load_file('simple_info_no_description.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_licence(self):
        xml = self.load_file('simple_info_no_licence.xml')
        result = self.parser.parse(xml)
        self.assertEqual(6, result['licence'])

    def test_simple_no_name(self):
        xml = self.load_file('simple_info_no_name.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_requiremin(self):
        xml = self.load_file('simple_info_no_requiremin.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_version(self):
        xml = self.load_file('simple_info_no_version.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_unknown_category(self):
        xml = self.load_file('simple_info_unknown_category.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

    def test_simple_no_unknown_licence(self):
        xml = self.load_file('simple_info_unknown_licence.xml')
        with self.assertRaises(DependencyError):
            self.parser.parse(xml)

if __name__ == '__main__':
    unittest.main()