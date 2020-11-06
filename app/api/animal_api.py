"""
    유기동물 api 정의
    5hyunq
    2020.11.01
    sample url: http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?serviceKey=[secret key]
"""

import configparser
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError
from xml.etree import ElementTree

config = configparser.ConfigParser()
config.read('config/config.ini')

def make_url(basic_url: str, query_data: dict):
    full_url = basic_url + "?"
    len_query = len(query_data)

    for index, (key, value) in enumerate(query_data.items()):
        if index == len_query-1:
            full_url += key + "=" + value
        else:
            full_url += key + "=" + value + "&"

    return full_url

def get_sido():
    url = config['API']['URL_SIDO']
    query_data = dict()
    query_data['serviceKey'] = config['API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        rslt = response.read()
        rslt = rslt.decode('utf-8')


        root_element = ElementTree.fromstring(rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['orgCd'] = element.find('orgCd').text
            rslt['orgdownNm'] = element.find('orgdownNm').text

            rslts.append(rslt)

        return rslts
    except URLError as e:
        print(e.reason)
        return e.reason



def get_sigungu(sido):
    url = config['API']['URL_SIGUNGU']

    input_data = dict()
    input_data['upr_cd'] = sido
    input_data['serviceKey'] = config['API']['APP_KEY']
    url_values = urlencode(input_data)
    full_url = url+'?'+url_values
    print(full_url)

    try:
        response = urlopen(full_url)
        print(response)
    except URLError as e:
        print(e.reason)

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

    try:
        response = urlopen(full_url)
        print(response)
    except URLError as e:
        print(e.reason)

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

    try:
        response = urlopen(full_url)
        print(response)
    except URLError as e:
        print(e.reason)
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

    try:
        response = urlopen(full_url)
        print(response)
    except URLError as e:
        print(e.reason)

    rslt = 0
    return rslt

