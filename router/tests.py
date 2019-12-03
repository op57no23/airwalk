from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.safari.webdriver import WebDriver 

class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_origin_destination(self):
        self.selenium.get('%s' % (self.live_server_url))
        origin = self.selenium.find_elements_by_class_name('mapboxgl-ctrl-geocoder--input')[0]
        destination = self.selenium.find_elements_by_class_name('mapboxgl-ctrl-geocoder--input')[1]
        origin.send_keys("Ohlone Elementary School, 950 Amarillo Ave, Palo Alto, California 94303, United States of America")
        destination.send_keys("Ohlone Elementary School, 950 Amarillo Ave, Palo Alto, California 94303, United States of America")
        self.selenium.find_element_by_tag_name('button').click()
        self.assertEqual(self.selenium.find_element_by_selector('ul li')[1].innerHTML, 'Time 0')


##Write a test case for gibberesh inputs and same origin and j
