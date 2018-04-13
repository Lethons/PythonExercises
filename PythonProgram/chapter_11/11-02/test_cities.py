import unittest
from city_functions import get_formatted_city


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = get_formatted_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted, 'Santiago, Chile - population 5000000')


unittest.main()
