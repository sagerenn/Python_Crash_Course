import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test the city_functions.py"""

    def test_city_country(self):
        """compare the city and country"""
        city_country_item = city_country('gz','china')
        self.assertEqual(city_country_item, 'Gz, China - population unknown')

    def test_city_country_population(self):
        """compare the city and country, population"""
        city_country_item = city_country('gz','china', 10000)
        self.assertEqual(city_country_item, 'Gz, China - population 10000')

if __name__ == '__main__':
    unittest.main()