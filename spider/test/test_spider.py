from unittest import TestCase

from spider.spider import Spider
from loguru import logger


class TestSpider(TestCase):
    def test_parse_courses(self):
        list = Spider().init()
        logger.debug('{_first_obj}, number of courses: {_number}'.format(_first_obj=list[0],_number=len(list)))

