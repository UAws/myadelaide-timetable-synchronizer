import os

import jwt
import requests
from dotenv import load_dotenv

from spider.adt.course import Course
from spider.adt.jwt_token import JwtToken
from loguru import logger

load_dotenv()

# https://curlconverter.com/
http_request_headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'application/json',
    'Authorization': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://myadelaide.uni.adelaide.edu.au',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://myadelaide.uni.adelaide.edu.au/',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
}


def preprocess_jwt_token():
    raw_token = os.getenv('MYADELAIDE_BEARER_TOKEN')
    if 'Bearer ' in raw_token:
        return raw_token.replace('Bearer ', '')
    else:
        return raw_token


class Spider:

    def __init__(self):
        self.jwt_token = preprocess_jwt_token()
        http_request_headers['Authorization'] = 'Bearer ' + self.jwt_token
        self.myadelaide_api_endpoint = os.getenv('TIMETABLE_API_ENDPOINT')
        self.student_id = self.decode_jwt_token()
        self.course_list = list()

    # example of decoded payload refer to adt.py --> jwt_token_data_type
    def decode_jwt_token(self):
        payload = jwt.decode(self.jwt_token, options={"verify_signature": False}, algorithms=["RS256"])

        # # https://stackoverflow.com/a/15882054/14207562
        # jwt_token = json.loads(payload, object_hook=lambda d: SimpleNamespace(**d))

        jwt_token = JwtToken.from_json_data(payload)

        # sub is the student id
        # The data in sub is in format of {a1xxxxxx}, remove a to match api path
        return jwt_token.sub.replace('a', '')

    # example of request url, week_id corresponding to number of weeks from current week, the current week maybe
    # variety due to different execution date
    # https://api.adelaide.edu.au/api/generic-query-structured/v1/?target=/system/TIMETABLE_WEEKLY/queryx/${
    # student_id},${week_id}&MaxRows=9999
    def generate_request_url(self, week_id):
        return self.myadelaide_api_endpoint \
               + '{student_id},{week}&MaxRows=9999'.format(student_id=self.student_id, week=week_id * 7)

    def retrieve_data_from_api(self):
        for x in range(52):

            # https://stackoverflow.com/a/6386366/14207562
            url = self.generate_request_url(week_id=x)
            resp = requests.get(url=url, headers=http_request_headers)
            data = resp.json()

            if resp.status_code != 200: logger.debug(data)

            if data['status'] == 'success':

                numbers_rows = data['data']['query']['numrows']

                logger.debug(
                    'week id : {_week_id}; number of course : {_numrows}'.format(_week_id=x, _numrows=numbers_rows))

                # only process when there are available course in this week
                if int(numbers_rows) > 0:
                    self.parse_courses(rows=data['data']['query']['rows'],
                                       numbers_rows=numbers_rows)

            else:
                raise ValueError('Could not retrieve data from api endpoint')

    def parse_courses(self, rows, numbers_rows):
        for i in range(int(numbers_rows)):
            self.course_list.append(Course.from_json_data(rows[i]))

    def get_course_list(self):
        return self.course_list

    def init(self):
        self.retrieve_data_from_api()
        return self.course_list
