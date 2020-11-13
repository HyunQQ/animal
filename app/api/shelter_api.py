"""
    유기동물 api 정의
    5hyunq
    2020.11.01
    sample url: http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?serviceKey=[secret key]
"""

import configparser
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree import ElementTree

from app.api.common import make_response, make_url

config = configparser.ConfigParser()
config.read('config/config.ini')

def get_shelter_info(querys):
    url = config['SHELTER_API']['URL_BASE'] + config['SHELTER_API']['URL_SHELTER_INFO']

    query_data = dict()
    for key, value in querys.items():
        query_data[key] = value

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

        rslts = []
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            rslt = {}
            rslt['orgCd'] = element.find('orgCd').text
            rslt['orgdownNm'] = element.find('orgdownNm').text

            rslts.append(rslt)

        response = make_response(response_data=rslts, info_data=info)

        return response
    except URLError as e:
        print(e.reason)
        return e.reason