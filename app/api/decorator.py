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

from functools import wraps
from rest_framework import request
from django.http import request
from django.http import QueryDict

from app.api.common import get_querys



def param_validator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(func.__name__)
        # print(get_querys(request))
        print(get_querys(self))
        return func(self, *args, **kwargs)
    return wrapper
