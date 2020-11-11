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

def make_response(response_data: dict=dict(), req_param: dict= dict()):
    response = dict()
    response['param'] = req_param
    response['rslt'] = response_data

    return response

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
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['orgCd'] = element.find('orgCd').text
            rslt['orgdownNm'] = element.find('orgdownNm').text

            rslts.append(rslt)

        response = make_response(response_data = rslts)

        return response
    except URLError as e:
        print(e.reason)
        return e.reason



def get_sigungu(upr_cd):
    url = config['API']['URL_SIGUNGU']

    query_data = dict()
    query_data['upr_cd'] = upr_cd
    req_param = query_data.copy()

    query_data['serviceKey'] = config['API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['orgCd'] = element.find('orgCd').text
            rslt['orgdownNm'] = element.find('orgdownNm').text

            rslts.append(rslt)

        response = make_response(response_data=rslts, req_param=req_param)

        return response
    except URLError as e:
        print(e.reason)
        return e.reason


def get_shelter(upr_cd, org_cd):
    url = config['API']['URL_SHELTER']

    query_data = dict()
    query_data['upr_cd'] = upr_cd
    query_data['org_cd'] = org_cd
    req_param = query_data.copy()

    query_data['serviceKey'] = config['API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['careNm'] = element.find('careNm').text
            rslt['careRegNo'] = element.find('careRegNo').text
            rslts.append(rslt)

        response = make_response(response_data=rslts, req_param=req_param)

        return response
    except URLError as e:
        print(e.reason)
        return e.reason


def get_kind(up_kind_cd):
    url = config['API']['URL_KIND']

    query_data = dict()
    query_data['up_kind_cd'] = up_kind_cd
    req_param = query_data.copy()

    query_data['serviceKey'] = config['API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['KNm'] = element.find('KNm').text
            rslt['kindCd'] = element.find('kindCd').text
            rslts.append(rslt)

        response = make_response(response_data=rslts, req_param=req_param)

        return response
    except URLError as e:
        print(e.reason)
        return e.reason


def get_abandonment(**kwargs):
    url = config['API']['URL_ABANDONMENT']

    query_data = dict()
    for key, item in kwargs.items():
        query_data[key] = item

    req_param = query_data.copy()
    query_data['serviceKey'] = config['API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['desertionNo'] = element.find('desertionNo').text
            rslt['filename'] = element.find('filename').text
            rslt['happenDt'] = element.find('happenDt').text
            rslt['happenPlace'] = element.find('happenPlace').text
            rslt['kindCd'] = element.find('kindCd').text
            rslt['colorCd'] = element.find('colorCd').text
            rslt['age'] = element.find('age').text
            rslt['weight'] = element.find('weight').text
            rslt['noticeNo'] = element.find('noticeNo').text
            rslt['noticeSdt'] = element.find('noticeSdt').text
            rslt['noticeEdt'] = element.find('noticeEdt').text
            rslt['popfile'] = element.find('popfile').text
            rslt['processState'] = element.find('processState').text
            rslt['sexCd'] = element.find('sexCd').text
            rslt['neuterYn'] = element.find('neuterYn').text
            rslt['specialMark'] = element.find('specialMark').text
            rslt['careNm'] = element.find('careNm').text
            rslt['careTel'] = element.find('careTel').text
            rslt['careAddr'] = element.find('careAddr').text
            rslt['orgNm'] = element.find('orgNm').text
            rslt['chargeNm'] = element.find('chargeNm').text
            rslt['officetel'] = element.find('officetel').text
            rslt['noticeComment'] = element.find('noticeComment').text

            rslts.append(rslt)

        # items 이외의 정보
        # rslt['numOfRows'] = element.find('numOfRows').text
        # rslt['pageNo'] = element.find('pageNo').text
        # rslt['totalCount'] = element.find('totalCount').text

        response = make_response(response_data=rslts, req_param=req_param)



        return response
    except URLError as e:
        print(e.reason)
        return e.reason

