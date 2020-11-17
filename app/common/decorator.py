"""
    decorator 정의
    5hyunq
    2020.11.16
"""

import os
import json

from functools import wraps
from jsonschema import ValidationError, validate

from app.common.common import get_querys
from app.common.result import bad_request


def param_validator(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print(func.__name__)
        print(get_querys(request))
        try:
            params = get_querys(request)
            file_nm = func.__name__ + "_validator.json"
            validator_file_path = os.path.join(os.getcwd(), 'app', 'validator', file_nm)
            if os.path.isfile(validator_file_path):
                validator_json = json.loads(open(validator_file_path).read())
                validate(params, validator_json)  ## validator 동작 원리 공부 필요

        except ValidationError as e:
            print(e.message)
            # logging
            return bad_request(msg=e.message)

        return func(request, *args, **kwargs)
    return wrapper


# class ParamValidator:
#     def __init__(self, function, request):
#         self.function = function
#         self.request = request
#
#     def __call__(self, *args, **kwargs):
#
#         print("전처리")
#         self.logging()
#         self.param_validator()
#         print(self.function(self.request, *args, **kwargs))
#         print("후처리")
#
#     def param_validator(self):
#         print("param validator word")
#         print(self.function.__name__)
#
#     def logging(self):
#         print("logger work")
