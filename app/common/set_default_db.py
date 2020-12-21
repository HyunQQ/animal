import configparser
from urllib.request import urlopen
from urllib.error import URLError
from xml.etree import ElementTree

from app.models.locations import Sido, Sigungu
from app.models.animal import KindCd
from app.common.common import make_url, check_none_info

config = configparser.ConfigParser()
config.read('config/config.ini')


def set_sido_info():
    api_sido_url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_SIDO']
    query_data = {
        'numOfRows': '20',
        "serviceKey": config['ANIMAL_API']['APP_KEY']
    }

    full_api_sido_url = make_url(api_sido_url, query_data)

    try:
        response = urlopen(full_api_sido_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            sido_cd = check_none_info(element.find('orgCd'))
            sido_nm = check_none_info(element.find('orgdownNm'))
            sido_inst = Sido.objects.create(sidoCd=sido_cd, sidoNm=sido_nm)
            set_sigungu_info(sido_inst)

    except URLError as e:
        print(e)

def set_sigungu_info(sido_inst):
    api_sigungu_url = config['ANIMAL_API']['URL_BASE'] + config['ANIMAL_API']['URL_SIGUNGU']
    query_data = {
        "upr_cd": sido_inst.sidoCd,
        "serviceKey": config['ANIMAL_API']['APP_KEY']
    }

    full_api_sigungu_url = make_url(api_sigungu_url, query_data)

    try:
        response = urlopen(full_api_sigungu_url)
        xml_rslt = response.read()
        xml_rslt = xml_rslt.decode('utf-8')

        root_element = ElementTree.fromstring(xml_rslt)
        iter_element = root_element.iter(tag='item')

        for element in iter_element:
            sigungu_cd = check_none_info(element.find('orgCd'))
            sigungu_nm = check_none_info(element.find('orgdownNm'))
            Sigungu.objects.create(sidoCd=sido_inst, sigunguCd=sigungu_cd, sigunguNm=sigungu_nm)

    except URLError as e:
        print(e)


def set_kind_info():
    data = {
        "417000": "개",
        "422400": "고양이",
        "429900": "기타"
    }

    for cd, nm in data.items():
        KindCd.objects.create(kindCd=cd, kindNm=nm)


if __name__ == "__main__":
    set_sido_info()
    set_kind_info()
