"""
    보호소 정보 api 정의
    5hyunq
    2020.11.13
"""

import configparser
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree import ElementTree

from app.common.common import make_url
from app.common.result import make_response_content

config = configparser.ConfigParser()
config.read('config/config.ini')


def get_shelter_detail(querys):
    url = config['SHELTER_API']['URL_BASE'] + config['SHELTER_API']['URL_SHELTER_INFO']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value

    req_param = query_data.copy()
    query_data['serviceKey'] = config['SHELTER_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)

        info = dict()
        info['resultCode'] = root_element.find('header').find('resultCode').text
        info['resultMsg'] = root_element.find('header').find('resultMsg').text
        info['numOfRows'] = root_element.find('body').find('numOfRows').text
        info['pageNo'] = root_element.find('body').find('pageNo').text
        info['totalCount'] = root_element.find('body').find('totalCount').text

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['breedCnt'] = element.find('breedCnt').text
            rslt['careAddr'] = element.find('careAddr').text
            rslt['careNm'] = element.find('careNm').text
            rslt['careTel'] = element.find('careTel').text
            rslt['closeDay'] = element.find('closeDay').text
            rslt['dataStdDt'] = element.find('dataStdDt').text
            rslt['divisionNm'] = element.find('divisionNm').text
            rslt['dsignationDate'] = element.find('dsignationDate').text
            rslt['feedCnt'] = element.find('feedCnt').text
            rslt['jibunAddr'] = element.find('jibunAddr').text
            rslt['lat'] = element.find('lat').text
            rslt['lng'] = element.find('lng').text
            rslt['medicalCnt'] = element.find('medicalCnt').text
            rslt['orgNm'] = element.find('orgNm').text
            rslt['quarabtineCnt'] = element.find('quarabtineCnt').text
            rslt['rnum'] = element.find('rnum').text
            rslt['saveTrgtAnimal'] = element.find('saveTrgtAnimal').text
            rslt['specsPersonCnt'] = element.find('specsPersonCnt').text
            rslt['vetPersonCnt'] = element.find('vetPersonCnt').text
            rslt['weekCellEtime'] = element.find('weekCellEtime').text
            rslt['weekCellStime'] = element.find('weekCellStime').text
            rslt['weekOprEtime'] = element.find('weekOprEtime').text
            rslt['weekOprStime'] = element.find('weekOprStime').text
            rslt['weekendCellEtime'] = element.find('weekendCellEtime').text
            rslt['weekendCellStime'] = element.find('weekendCellStime').text
            rslt['weekendOprEtime'] = element.find('weekendOprEtime').text
            rslt['weekendOprStime'] = element.find('weekendOprStime').text

            rslts.append(rslt)

        response = make_response_content(response_data=rslts, req_param=req_param, info_data=info)

        return response
    except URLError as e:
        reponse_data = {
            'Open API Server Error': e.reason
        }
        response = make_response_content(response_data=reponse_data, req_param=req_param)
        return response
