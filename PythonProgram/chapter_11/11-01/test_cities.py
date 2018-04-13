import unittest
from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')


unittest.main()
