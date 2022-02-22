from datetime import datetime
from unittest import TestCase

from s_calendar.calendar_generator import Calendar_generator
from spider.adt.course import Course

# sample data
course = Course.from_json_data({
    "attr:rownumber": 1,
    "A.EMPLID": "1xxxxxx",
    "A.STRM": "4210",
    "D.XLATLONGNAME": "Practical",
    "START_TIME": "13.00",
    "END_TIME": "11.00",
    "B.SUBJECT": "COMP SCI",
    "B.CATALOG_NBR": "3303",
    "B.DESCR": "Engineering Software as Serv I",
    "F.DESCR": "Barr Smith South",
    "E.ROOM": "2060",
    "E.DESCR": "Teaching Room",
    "C.WEEKDAY_NAME": "Monday",
    "DATE": "28 Feb 2022",
    "B.CRSE_ID": "107926",
    "C.SORT_ORDER": 1
})


class TestCalendar(TestCase):
    def test_generate_calendar(self):
        # course_name = ''
        # course_name = map(
        #     lambda word: word[0].upper(),
        #     course.b_descr.split()
        # )

        course_name = ''.join(str(word)[0].upper() for word in course.b_descr.split())

        print(course_name)

    def test_date(self):
        # https://www.programiz.com/python-programming/datetime/strftime
        timestamp = datetime.strptime(course.date + ' ' + course.start_time, '%d %b %Y %H.%M')

        # print('{}{}{} {}{}{}')

        print(str(timestamp))

        utc = Calendar_generator._time_converter(course.date, course.start_time)
        print(utc)
