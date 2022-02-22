import json

import pathlib

from utils.shell_executor.executor import execute_now

course_abstract_data_type = {
    "attr:rownumber": 1,
    "A.EMPLID": "1xxxxxx",
    "A.STRM": "4210",
    "D.XLATLONGNAME": "Practical",
    "START_TIME": "09.00",
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
}

jwt_token_abstract_data_type = {
    "ver": 1,
    "jti": "AT.FcWt_X10TfWdKNE9e-k8UezMEUls8FpvENn0y846-4k",
    "iss": "https://adelaide.okta.com/oauth2/default",
    "aud": "api://default",
    "iat": 1645433032,
    "exp": 1645436632,
    "cid": "0oaiku3xxvUYEFpAR3l6",
    "uid": "00u7je955ZI8OpVQm3l6",
    "scp": [
        "email",
        "openid",
        "profile"
    ],
    "sub": "a1xxxxxx"
}


# https://github.com/bcwaldon/warlock
def generate_schemes(json_data):
    for key in json_data:
        json_data[key] = {'type': 'string'}

    result = {'properties': json_data}

    return json.dumps(result)

    # https://github.com/jsontypedef/json-typedef-codegen


def generate_schemes_by_jtd_codegen(data_type, name):

    current_dir = pathlib.Path().resolve()

    execute_now('cd {_current_dir};'
                'rm -rf {_name};'
                'rm -rf {_name}.json'.format(_name=name, _current_dir=current_dir))

    f = open(name + ".json", "w")
    f.write(generate_schemes(json_data=data_type))
    f.close()

    execute_now('cd {_current_dir} ;'
                'mkdir {_name} ;'
                'jtd-codegen {_name}.json --python-out {_name};'
                'rm -rf {_name}.json'
                .format(_current_dir=current_dir, _name=name))
