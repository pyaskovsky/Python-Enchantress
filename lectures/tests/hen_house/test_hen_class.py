import unittest
from unittest import mock
from unittest.mock import patch
from lectures.tests.hen_house.hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        # optional method, may be used to initialize hen_house instance

        self.hen_house = HenHouse(10)

    def test_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised

        with self.assertRaises(ValueError) as e:
            self.hen_house.__init__(4)

    def test_season(self):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons

        with patch('lectures.tests.hen_house.hen_class.datetime.datetime') as mock_data:
            mock_data.today().month = 4
            self.assertEqual(self.hen_house.season, 'spring')

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'spring')
    def test_productivity_index(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute

        self.assertEqual(self.hen_house._productivity_index(), self.hen_house.hens_productivity.get('spring'))

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'april')
    def test_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called

        self.assertRaises(ErrorTimesOfYear, lambda: self.hen_house._productivity_index())

    @patch('lectures.tests.hen_house.hen_class.HenHouse._productivity_index', mock.Mock(return_value=0.5))
    def test_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked

        self.assertEqual(self.hen_house.get_eggs_daily(6), 3)

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'spring')
    def test_get_max_count_for_soup(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future

        self.assertEqual(self.hen_house.get_max_count_for_soup(2), 6)

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'spring')
    def test_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future

        self.assertEqual(self.hen_house.get_max_count_for_soup(10), 0)

    def test_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type

        with patch('lectures.tests.hen_house.hen_class.requests.get') as mock_data:
            mock_data.return_value.status_code = 200
            self.assertTrue(self.hen_house.food_price())

    def test_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called

        with patch('lectures.tests.hen_house.hen_class.requests.get') as response:
            response.return_value.status_code = 0
            with self.assertRaises(ConnectionError):
                self.hen_house.food_price()


if __name__ == '__main__':
    unittest.main()
