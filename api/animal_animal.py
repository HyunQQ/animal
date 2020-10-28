"""
sample
http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?serviceKey=[secret key]
"""

import configparser
from urllib.request import urlopen
from urllib.parse import urlencode

config = configparser.ConfigParser()
config.read('config/config.ini')


def get_sido():
    url = config['API']['URL_SIDO']

    input_data = dict()
    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)

    full_url = url+'?'+url_values
    print(full_url)

    response = urlopen(full_url)
    print(response)

    rslt=0
    return rslt


def get_sigungu(sido):
    url = config['API']['URL_SIGUNGU']

    input_data = dict()
    input_data['upr_cd'] = sido
    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)

    full_url = url+'?'+url_values
    print(full_url)

    response = urlopen(full_url)
    print(response)

    rslt = 0
    return rslt

def get_shelter(sido, sigungu):
    url = config['API']['URL_SHELTER']

    input_data = dict()
    input_data['upr_cd'] = sido
    input_data['org_cd'] = sigungu
    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)

    full_url = url+'?'+url_values
    print(full_url)

    response = urlopen(full_url)
    print(response)

    rslt = 0
    return rslt

def get_kind(up_kind_cd):
    url = config['API']['URL_KIND']

    input_data = dict()
    input_data['up_kind_cd'] = up_kind_cd
    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)

    full_url = url+'?'+url_values
    print(full_url)

    response = urlopen(full_url)
    print(response)
    rslt = 0
    return rslt

def get_abandonment(bgnde, endde, pageNo, numOfRows):
    url = config['API']['URL_ABANDONMENT']

    input_data = dict()
    input_data['bgnde'] = bgnde
    input_data['endde'] = endde
    input_data['pageNo'] = pageNo
    input_data['numOfRows'] = numOfRows

    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)

    full_url = url+'?'+url_values
    print(full_url)

    response = urlopen(full_url)
    print(response)

    rslt = 0
    return rslt

