from ics import Calendar, Event
from typing import List

from spider.adt.course import Course
from datetime import datetime
import pytz


class Calendar_generator:

    #     type support  https://stackoverflow.com/a/21384492/14207562
    @classmethod
    def generate_calendar(cls, course_list: List[Course]):
        _calendar = Calendar()

        for course in course_list:
            # event api : https://icspy.readthedocs.io/en/stable/api.html#event
            # format reference: official UOFA timetable
            # reference UI : https://minio.llycloud.com/image/uPic/image-20220223KbYC2h.png
            course_event = Event(
                # abbreviation by first character of the course description
                name=
                ''.join(str(word)[0].upper() for word in course.b_descr.replace('UG', '').replace('&', '').split())
                + ' ' + course.d_xlatlongname
                ,
                # date convert
                # https://stackoverflow.com/a/466376/14207562
                # time zone configuration required
                # https://stackoverflow.com/a/79877/14207562
                begin=cls._time_converter(course.date, course.start_time),

                end=cls._time_converter(course.date, course.end_time),

                description='{_subject} {_course_number} - {_course_description} '.format(
                    _subject=course.b_subject,
                    _course_number=course.a_strm,
                    _course_description=course.b_descr
                ),

                location='{_building}/{_room_number}/{_room_description}'.format(
                    _building=course.f_descr,
                    _room_number=course.b_catalog_nbr,
                    _room_description=course.e_descr
                )
            )

            _calendar.events.add(course_event)

        with open('my.ics', 'w') as f:
            # https://github.com/ics-py/ics-py/issues/316#issue-1144819148
            f.write(str(_calendar))
            # And it's done !

            # iCalendar-formatted data is also available in a string
            # str(c)
            # 'BEGIN:VCALENDAR\nPRODID:...

    @classmethod
    def _time_converter(cls, date, time):
        # https://stackoverflow.com/a/79877/14207562
        local = pytz.timezone("Australia/Adelaide")
        naive = datetime.strptime(date + ' ' + time, '%d %b %Y %H.%M')
        local_dt = local.localize(naive, is_dst=None)
        utc_dt = local_dt.astimezone(pytz.utc)
        return utc_dt
