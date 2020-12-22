from app.models.locations import Sido, Sigungu
from app.api.animal_api import get_shelter
from app.common.result import make_response_content


def get_shelter_nearby(querys: dict):
    # ex location : 경기도 양주시 남면 감악산로 63-37 (남면) 한국동물구조관리협회
    # 경상남도 창원시 마산합포구 진북면 지산2길 139-112 226-19
    location = querys['location']
    sub_location = location.split()
    sido = sub_location[0]
    sigungu = sub_location[1]

    if "창원" in sigungu:
        sigungu = sub_location[1][:2] + " " + sub_location[2][:2]


    try:
        data = dict()
        data['upr_cd'] = Sido.objects.values_list('sidoCd', flat=True).filter(sidoNm__contains=sido)[0]
        data['org_cd'] = Sigungu.objects.values_list('sigunguCd', flat=True).filter(sigunguNm__contains=sigungu)[0]
        response = get_shelter(data)

    except:
        reponse_data = {
            'Open API Server Error': 'Cannot get data in DB.'
        }
        response = make_response_content(response_data=reponse_data, req_param=querys)

    return response


def get_action_guide():
    return 0


def get_characteristic_kind(up_kind_cd, kind_cd):
    return 0


