# selenium 4
# https://github.com/SergeyPirogov/webdriver_manager
# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# https://pypi.org/project/selenium-wire/

import time
from loguru import logger
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium_controller.driver import driver


class AutoAuth:

    def __init__(self):

        self.driver = driver
        self.jwt_token = ''

    # This function will wait for login to myadelaide panel and retrieve the authorization Bearer from header
    # the stop condition is api.adelaide.edu.au has been accessed with Authorization header
    def _wait_until_login_to_myadelaide(self):

        while True:

            time.sleep(1)

            for request in self.driver.requests:
                if request.response:

                    auth = request.headers['Authorization']
                    if 'api.adelaide.edu.au' in str(request.url) \
                            and auth is not None:
                        logger.debug(request.url)
                        logger.debug(auth)

                        self.jwt_token = auth

                        # https://stackoverflow.com/a/21038589/14207562
                        return expected_conditions.url_contains('adelaide.edu.au')

    def open_browser(self, url):

        self.driver.get(url)

        WebDriverWait(self.driver, timeout=30 * 5).until(self._wait_until_login_to_myadelaide())

    def init(self):

        self.open_browser(url='https://myadelaide.uni.adelaide.edu.au/')

        return self.jwt_token
