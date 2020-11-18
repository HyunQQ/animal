"""
    decorator 정의
    5hyunq
    2020.11.16
"""

import os
import json
import logging
from pprint import pformat
from functools import wraps
from jsonschema import ValidationError, validate

from app.common.common import get_querys
from app.common.result import bad_request


def param_validator(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logging.info("Client call url : {}".format(request.path))
        try:
            params = get_querys(request)
            file_nm = func.__name__ + "_validator.json"
            validator_file_path = os.path.join(os.getcwd(), 'app', 'validator', file_nm)
            if os.path.isfile(validator_file_path):
                validator_json = json.loads(open(validator_file_path).read())
                logging.debug("Requested Query param : \n{}".format(pformat(params)))
                logging.debug("Validator Json : \n{}".format(pformat(validator_json)))
                validate(params, validator_json)

        except ValidationError as e:
            logging.exception(e.message)
            return bad_request(msg=e.message)

        return func(request, *args, **kwargs)
    return wrapper
