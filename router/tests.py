from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver 
import time
import pdb

class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_origin_destination(self):
        self.selenium.get('%s' % (self.live_server_url))
        origin = self.selenium.find_elements_by_class_name('mapboxgl-ctrl-geocoder--input')[0]
        destination = self.selenium.find_elements_by_class_name('mapboxgl-ctrl-geocoder--input')[1]
        origin.send_keys("Ohlone Elementary School, 950 Amarillo Ave, Palo Alto, California 94303, United States of America")
        self.selenium.find_element_by_css_selector('#origin ul li a').click()
        destination.send_keys("Ohlone Elementary School, 950 Amarillo Ave, Palo Alto, California 94303, United States of America")
        self.selenium.find_element_by_css_selector('#destination ul li a').click()
        self.assertFalse(self.selenium.find_element_by_css_selector('#routebutton button').is_enabled())
        
        destination.clear()
        destination.send_keys("Duveneck Elementary, 705 Alester Ave, Palo Alto, California 94303, United States of America")
        time.sleep(3)
        self.selenium.find_element_by_css_selector('#destination ul li a').click()

        time.sleep(3)
        self.assertTrue(self.selenium.find_element_by_css_selector('#routebutton button').is_enabled())

### Testing out of bounds
        self.selenium.find_element_by_css_selector('#routebutton button').click()
        self.selenium.find_element_by_css_selector('.results button').click()
        self.assertTrue('outside of the bounds' in self.selenium.find_element_by_css_selector('.results .card-body .card-subtitle').text)
