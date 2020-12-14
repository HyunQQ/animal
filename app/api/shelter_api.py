"""
    보호소 정보 api 정의
    5hyunq
    2020.11.13
"""

import configparser
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree import ElementTree

from app.common.common import make_url, check_none_info
from app.common.result import make_response_content

config = configparser.ConfigParser()
config.read('config/config.ini')


# new version
def get_shelter_detail(care_reg_no):
    url = config['SHELTER_API']['URL_BASE'] + config['SHELTER_API']['URL_SHELTER_INFO']

    query_data = dict()
    query_data['care_reg_no'] = care_reg_no
    query_data['serviceKey'] = config['SHELTER_API']['APP_KEY']
    full_url = make_url(url, query_data)

    try:
        response = urlopen(full_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        rslt = dict()

        if root_element.find('body').find('items').find('item') is None:
            rslt['breedCnt'] = ""
            rslt['careAddr'] = ""
            # rslt['careNm'] = ""
            rslt['careTel'] = ""
            rslt['closeDay'] = ""
            rslt['dataStdDt'] = ""
            rslt['divisionNm'] = ""
            rslt['dsignationDate'] = ""
            rslt['feedCnt'] = ""
            rslt['jibunAddr'] = ""
            rslt['lat'] = ""
            rslt['lng'] = ""
            rslt['medicalCnt'] = ""
            rslt['orgNm'] = ""
            rslt['quarabtineCnt'] = ""
            rslt['rnum'] = ""
            rslt['saveTrgtAnimal'] = ""
            rslt['specsPersonCnt'] = ""
            rslt['vetPersonCnt'] = ""
            rslt['weekCellEtime'] = ""
            rslt['weekCellStime'] = ""
            rslt['weekOprEtime'] = ""
            rslt['weekOprStime'] = ""
            rslt['weekendCellEtime'] = ""
            rslt['weekendCellStime'] = ""
            rslt['weekendOprEtime'] = ""
            rslt['weekendOprStime'] = ""
        else:
            element = root_element.find('body').find('items').find('item')

            rslt['breedCnt'] = check_none_info(element.find('breedCnt'))
            rslt['careAddr'] = check_none_info(element.find('careAddr'))
            # rslt['careNm'] = check_none_info(element.find('careNm'))
            rslt['careTel'] = check_none_info(element.find('careTel'))
            rslt['closeDay'] = check_none_info(element.find('closeDay'))
            rslt['dataStdDt'] = check_none_info(element.find('dataStdDt'))
            rslt['divisionNm'] = check_none_info(element.find('divisionNm'))
            rslt['dsignationDate'] = check_none_info(element.find('dsignationDate'))
            rslt['feedCnt'] = check_none_info(element.find('feedCnt'))
            rslt['jibunAddr'] = check_none_info(element.find('jibunAddr'))
            rslt['lat'] = check_none_info(element.find('lat'))
            rslt['lng'] = check_none_info(element.find('lng'))
            rslt['medicalCnt'] = check_none_info(element.find('medicalCnt'))
            rslt['orgNm'] = check_none_info(element.find('orgNm'))
            rslt['quarabtineCnt'] = check_none_info(element.find('quarabtineCnt'))
            rslt['rnum'] = check_none_info(element.find('rnum'))
            rslt['saveTrgtAnimal'] = check_none_info(element.find('saveTrgtAnimal'))
            rslt['specsPersonCnt'] = check_none_info(element.find('specsPersonCnt'))
            rslt['vetPersonCnt'] = check_none_info(element.find('vetPersonCnt'))
            rslt['weekCellEtime'] = check_none_info(element.find('weekCellEtime'))
            rslt['weekCellStime'] = check_none_info(element.find('weekCellStime'))
            rslt['weekOprEtime'] = check_none_info(element.find('weekOprEtime'))
            rslt['weekOprStime'] = check_none_info(element.find('weekOprStime'))
            rslt['weekendCellEtime'] = check_none_info(element.find('weekendCellEtime'))
            rslt['weekendCellStime'] = check_none_info(element.find('weekendCellStime'))
            rslt['weekendOprEtime'] = check_none_info(element.find('weekendOprEtime'))
            rslt['weekendOprStime'] = check_none_info(element.find('weekendOprStime'))

        return rslt
    except URLError as e:
        return e.reason


# ori version

#
# def get_shelter_detail(querys):
#     url = config['SHELTER_API']['URL_BASE'] + config['SHELTER_API']['URL_SHELTER_INFO']
#
#     query_data = dict()
#     for key, value in querys.items():
#         query_data[key] = value
#
#     req_param = query_data.copy()
#     query_data['serviceKey'] = config['SHELTER_API']['APP_KEY']
#     full_url = make_url(url, query_data)
#
#     try:
#         response = urlopen(full_url)
#         xml_rslt = response.read()
#         xml_rslt = xml_rslt.decode('utf-8')
#
#         root_element = ElementTree.fromstring(xml_rslt)
#
#         info = dict()
#         info['resultCode'] = check_none_info(root_element.find('header').find('resultCode'))
#         info['resultMsg'] = check_none_info(root_element.find('header').find('resultMsg'))
#         info['numOfRows'] = check_none_info(root_element.find('body').find('numOfRows'))
#         info['pageNo'] = check_none_info(root_element.find('body').find('pageNo'))
#         info['totalCount'] = check_none_info(root_element.find('body').find('totalCount'))
#
#         rslts = []
#         iter_element = root_element.iter(tag='item')
#
#         for element in iter_element:
#             rslt = dict()
#             rslt['breedCnt'] = check_none_info(element.find('breedCnt'))
#             rslt['careAddr'] = check_none_info(element.find('careAddr'))
#             rslt['careNm'] = check_none_info(element.find('careNm'))
#             rslt['careTel'] = check_none_info(element.find('careTel'))
#             rslt['closeDay'] = check_none_info(element.find('closeDay'))
#             rslt['dataStdDt'] = check_none_info(element.find('dataStdDt'))
#             rslt['divisionNm'] = check_none_info(element.find('divisionNm'))
#             rslt['dsignationDate'] = check_none_info(element.find('dsignationDate'))
#             rslt['feedCnt'] = check_none_info(element.find('feedCnt'))
#             rslt['jibunAddr'] = check_none_info(element.find('jibunAddr'))
#             rslt['lat'] = check_none_info(element.find('lat'))
#             rslt['lng'] = check_none_info(element.find('lng'))
#             rslt['medicalCnt'] = check_none_info(element.find('medicalCnt'))
#             rslt['orgNm'] = check_none_info(element.find('orgNm'))
#             rslt['quarabtineCnt'] = check_none_info(element.find('quarabtineCnt'))
#             rslt['rnum'] = check_none_info(element.find('rnum'))
#             rslt['saveTrgtAnimal'] = check_none_info(element.find('saveTrgtAnimal'))
#             rslt['specsPersonCnt'] = check_none_info(element.find('specsPersonCnt'))
#             rslt['vetPersonCnt'] = check_none_info(element.find('vetPersonCnt'))
#             rslt['weekCellEtime'] = check_none_info(element.find('weekCellEtime'))
#             rslt['weekCellStime'] = check_none_info(element.find('weekCellStime'))
#             rslt['weekOprEtime'] = check_none_info(element.find('weekOprEtime'))
#             rslt['weekOprStime'] = check_none_info(element.find('weekOprStime'))
#             rslt['weekendCellEtime'] = check_none_info(element.find('weekendCellEtime'))
#             rslt['weekendCellStime'] = check_none_info(element.find('weekendCellStime'))
#             rslt['weekendOprEtime'] = check_none_info(element.find('weekendOprEtime'))
#             rslt['weekendOprStime'] = check_none_info(element.find('weekendOprStime'))
#
#             rslts.append(rslt)
#
#         response = make_response_content(response_data=rslts, req_param=req_param, info_data=info)
#
#         return response
#     except URLError as e:
#         reponse_data = {
#             'Open API Server Error': e.reason
#         }
#         response = make_response_content(response_data=reponse_data, req_param=req_param)
#         return response