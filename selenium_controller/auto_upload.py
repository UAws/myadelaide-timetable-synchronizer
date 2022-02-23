from datetime import datetime
from sys import platform
import pathlib
import time
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui
from selenium_controller.driver import driver


class AutoUpload:

    def __init__(self):
        self.driver = driver
        self.jwt_token = ''

    def __del__(self):
        self.driver.close()

    def upload(self):
        self.driver.get("https://outlook.office365.com/owa/adelaide.edu.au")

        now = datetime.now()

        calendar_name = 'Course Timetable {_year} semester {_number}'.format(_year=now.year,
                                                                             _number=1 if now.month < 7 else 2)

        # Step # | name | target | value
        # 1 | open | /calendar/view/week |
        self.driver.get("https://outlook.office.com/calendar/view/week")
        # 2 | setWindowSize | 2304x1271 |
        self.driver.set_window_size(1920, 1080)
        # 3 | runScript | window.scrollTo(0,0) |
        self.driver.execute_script("window.scrollTo(0,0)")
        # 4 | click | xpath=//div[@id='leftPaneContainer']/div/div[3]/div/div/button/span |
        self._wait_until_find(By.XPATH, "//div[3]/div/div/button/span").click()
        # 5 | click | xpath=//button[@id='CreateCalendar']/span |
        self._wait_until_find(By.XPATH, "//button[@id=\'CreateCalendar\']/span").click()
        # 6 | type | xpath=//div[2]/div/div/div/div/input | Test
        self._wait_until_find(By.XPATH, "//div[2]/div/div/div/div/input").send_keys(
            calendar_name)
        # 7 | click | xpath=//div[6]/div/div/button/span/span |
        self._wait_until_find(By.XPATH, "//div[6]/div/div/button/span/span").click()
        # 8 | click | xpath=//button[@id='ImportFromFile']/span/div |
        self._wait_until_find(By.XPATH, "//button[@id=\'ImportFromFile\']/span/div").click()

        # self.driver.execute_script("""
        #         document.addEventListener('click', function(evt) {
        #           if (evt.target.type === 'file')
        #             evt.preventDefault();
        #         }, true)
        #
        #         document.querySelectorAll('input')[1].disabled = false;
        #         """)
        # 9 | click | xpath=//div[2]/div/div/div/div[2]/div/button/span/span/span |
        # self._wait_until_find(By.XPATH, "//div[2]/div/div/div/div[2]/div/button/span/span/span").click()

        # https://stackoverflow.com/a/58051573/14207562
        # pyautogui.write('{current_dir}/my.ics'.format(current_dir=pathlib.Path().resolve()))
        # pyautogui.press('enter')

        # 10 | type | xpath=//div[2]/div/input | /Users/akide/Downloads/my.ics
        self.driver.find_element(By.XPATH, "//div[2]/div/input").send_keys(
            '{current_dir}/my.ics'.format(current_dir=pathlib.Path().resolve()))

        # 11 | click | xpath=//span[contains(.,'Select a calendar')] |
        self._wait_until_find(By.XPATH, "//span[contains(.,\'Select a calendar\')]").click()
        time.sleep(1)

        # 12 | click | xpath=//div[6]/div/div/div/div/div/div/button[4]/span |
        self.driver.find_elements_by_xpath("//button/span[contains(.,\'{name}\')]".format(name=calendar_name))[
            1].click()
        # 13 | click | xpath=//div[3]/div/div/button/span/span/span |
        self._wait_until_find(By.XPATH, "//div[3]/div/div/button/span/span/span").click()

        # wait for upload ics

        WebDriverWait(self.driver, timeout=30 * 5).until(self._wait_until_ics_uploaded())

    # http://allselenium.info/wait-for-elements-python-selenium-webdriver
    def _wait_until_find(self, by=By.ID, value=None):
        return WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((by, value)))

    def _wait_until_ics_uploaded(self):

        while True:
            time.sleep(1)
            for request in self.driver.requests:
                if request.response:
                    if request.response.status_code == 200 and 'action=ImportCalendarEvent' in request.url:
                        # https://stackoverflow.com/a/21038589/14207562
                        return expected_conditions.url_contains('outlook.office.com')
