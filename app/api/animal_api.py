"""
    유기동물 api 정의
    5hyunq
    2020.11.01
"""

import configparser
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree import ElementTree

from app.common.common import make_url, check_none_info
from app.common.result import make_response_content
from app.api.shelter_api import get_shelter_detail

config = configparser.ConfigParser()
config.read('config/config.ini')


def get_sido(querys):
    url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_SIDO']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value

    req_param = query_data.copy()
    query_data['serviceKey'] = config['ANIMAL_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)

        info = dict()
        info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
        info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))
        info['numOfRows'] = check_none_info(root_element.find('body').find('numOfRows'))
        info['pageNo'] = check_none_info(root_element.find('body').find('pageNo'))
        info['totalCount'] = check_none_info(root_element.find('body').find('totalCount'))

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = dict()
            rslt['orgCd'] = check_none_info(element.find('orgCd'))
            rslt['orgdownNm'] = check_none_info(element.find('orgdownNm'))

            rslts.append(rslt)

        response = make_response_content(response_data = rslts, req_param=req_param, info_data=info)

        return response
    except URLError as e:
        reponse_data = {
            'Open API Server Error' : e.reason
        }
        response = make_response_content(response_data= reponse_data, req_param=req_param)
        return response


def get_sigungu(querys):
    url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_SIGUNGU']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value

    req_param = query_data.copy()

    query_data['serviceKey'] = config['ANIMAL_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        info = dict()
        info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
        info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))


        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = dict()
            rslt['orgCd'] = check_none_info(element.find('orgCd'))
            rslt['orgdownNm'] = check_none_info(element.find('orgdownNm'))

            rslts.append(rslt)

        response = make_response_content(response_data=rslts, req_param=req_param, info_data=info)

        return response
    except URLError as e:
        reponse_data = {
            'Open API Server Error': e.reason
        }
        response = make_response_content(response_data=reponse_data, req_param=req_param)
        return response


def get_shelter(querys):
    url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_SHELTER']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value
    req_param = query_data.copy()

    query_data['serviceKey'] = config['ANIMAL_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        info = dict()
        info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
        info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = dict()
            rslt['careNm'] = check_none_info(element.find('careNm'))
            rslt['careRegNo'] = check_none_info(element.find('careRegNo'))
            shelter_detail_info = get_shelter_detail(rslt['careRegNo'])
            if isinstance(shelter_detail_info, dict):
                rslt.update(shelter_detail_info)
            else:
                info['resultMsg'] = "SHELTER DETAIL API ERROR : " + shelter_detail_info

            rslts.append(rslt)

        response = make_response_content(response_data=rslts, req_param=req_param, info_data=info)

        return response
    except URLError as e:
        reponse_data = {
            'Open API Server Error': e.reason
        }
        response = make_response_content(response_data=reponse_data, req_param=req_param)
        return response


def get_kind(querys):
    url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_KIND']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value
    req_param = query_data.copy()

    query_data['serviceKey'] = config['ANIMAL_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)

        info = dict()
        info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
        info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = dict()
            rslt['KNm'] = check_none_info(element.find('KNm'))
            rslt['kindCd'] = check_none_info(element.find('kindCd'))
            rslts.append(rslt)

        response = make_response_content(response_data=rslts, req_param=req_param,info_data=info)

        return response
    except URLError as e:
        reponse_data = {
            'Open API Server Error': e.reason
        }
        response = make_response_content(response_data=reponse_data, req_param=req_param)
        return response


def get_abandonment(querys):
    url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_ABANDONMENT']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value

    req_param = query_data.copy()
    query_data['serviceKey'] = config['ANIMAL_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        info = dict()
        info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
        info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))
        info['numOfRows'] = check_none_info(root_element.find('body').find('numOfRows'))
        info['pageNo'] = check_none_info(root_element.find('body').find('pageNo'))
        info['totalCount'] = check_none_info(root_element.find('body').find('totalCount'))

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = dict()
            rslt['desertionNo'] = check_none_info(element.find('desertionNo'))
            rslt['filename'] = check_none_info(element.find('filename'))
            rslt['happenDt'] = check_none_info(element.find('happenDt'))
            rslt['happenPlace'] = check_none_info(element.find('happenPlace'))
            rslt['kindCd'] = check_none_info(element.find('kindCd'))
            rslt['colorCd'] = check_none_info(element.find('colorCd'))
            rslt['age'] = check_none_info(element.find('age'))
            rslt['weight'] = check_none_info(element.find('weight'))
            rslt['noticeNo'] = check_none_info(element.find('noticeNo'))
            rslt['noticeSdt'] = check_none_info(element.find('noticeSdt'))
            rslt['noticeEdt'] = check_none_info(element.find('noticeEdt'))
            rslt['popfile'] = check_none_info(element.find('popfile'))
            rslt['processState'] = check_none_info(element.find('processState'))
            rslt['sexCd'] = check_none_info(element.find('sexCd'))
            rslt['neuterYn'] = check_none_info(element.find('neuterYn'))
            rslt['specialMark'] = check_none_info(element.find('specialMark'))
            rslt['careNm'] = check_none_info(element.find('careNm'))
            rslt['careTel'] = check_none_info(element.find('careTel'))
            rslt['careAddr'] = check_none_info(element.find('careAddr'))
            rslt['orgNm'] = check_none_info(element.find('orgNm'))
            rslt['chargeNm'] = check_none_info(element.find('chargeNm'))
            rslt['officetel'] = check_none_info(element.find('officetel'))
            rslts.append(rslt)

        response = make_response_content(response_data=rslts, req_param=req_param, info_data = info)
        return response

    except URLError as e:
        reponse_data = {
            'Open API Server Error': e.reason
        }
        response = make_response_content(response_data=reponse_data, req_param=req_param)
        return response


