import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')
