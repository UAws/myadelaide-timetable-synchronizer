from unittest import TestCase

from selenium_controller.auto_auth import AutoAuth


class Test(TestCase):
    def test_open_browser(self):
        AutoAuth().open_browser(url='https://myadelaide.uni.adelaide.edu.au/')
