"""
    response 형태 정의
    5hyunq
    2020.11.17
"""

import datetime

from rest_framework import status
from rest_framework.response import Response


def make_response_content(info_data: dict, response_data: dict=dict(), req_param: dict= dict()):
    response_content = {
        'param' : req_param,
        'info'  : info_data,
        'rslt'  : response_data
    }

    return response_content


def ok(content):
    resp = {
        'status'    : status.HTTP_200_OK,
        'message'   : 'Request OK',
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content'   : content
    }
    # logging
    return Response(resp, status=status.HTTP_200_OK)


def created(content):
    resp = {
        'status'    : status.HTTP_201_CREATED,
        'message'   : 'Create Success',
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content'   : content
    }
    # logging
    return Response(resp, status=status.HTTP_201_CREATED)


def not_found(content):
    resp = {
        'status'    : status.HTTP_404_NOT_FOUND,
        'message'   : 'Not Found Content',
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content'   : content
    }
    # logging
    return Response(resp, status=status.HTTP_404_NOT_FOUND)


def bad_request(msg : str):
    resp = {
        'status'    : status.HTTP_400_BAD_REQUEST,
        'message'   : 'Invalid Parameter : ' + msg,
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    # logging
    return Response(resp, status=status.HTTP_400_BAD_REQUEST)


def error(content, msg : str):
    resp = {
        'status'    : status.HTTP_500_INTERNAL_SERVER_ERROR,
        'message'   : 'Internal Server Error : ' + msg,
        'timestamp' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content'   : content
    }
    # logging
    return Response(resp, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

