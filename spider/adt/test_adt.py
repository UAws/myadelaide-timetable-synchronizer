from unittest import TestCase

from spider.adt.adt import generate_schemes, course_abstract_data_type, generate_schemes_by_jtd_codegen, \
    jwt_token_abstract_data_type


class Test(TestCase):
    def test_generate_schemes(self):
        print(generate_schemes(json_data=course_abstract_data_type))

    def test_generate_course_schemes(self):
        generate_schemes_by_jtd_codegen(course_abstract_data_type, 'course')

    def test_generate_jwt_token_schemes(self):
        generate_schemes_by_jtd_codegen(jwt_token_abstract_data_type, 'jwt_token')
